''' callcontract.py - デプロイしたコントラクトを呼び出す '''

import os
from web3 import Web3
from web3.contract import Contract

kovan_url = os.getenv('KOVAN_URL')
cname = os.getenv('CONTRACTNAME')

address_file = cname + '.address'
abi_file = cname + '.abi'

w3 = Web3(Web3.HTTPProvider(kovan_url))

print('w3.isConnected:', w3.isConnected())

''' コントラクトアドレスの読み出し '''
with open(address_file, mode='rt') as fp:
    hwadd = fp.read()

''' ABIの読み出し '''
with open(abi_file, mode='rt') as fp:
    abi = fp.read()

''' コントラクトオブジェクトの作成 '''
contract = w3.eth.contract(hwadd, abi=abi)

''' 関数を指定 '''
c_func = contract.functions.getLatestPrice()

''' コントラクト関数の呼び出し '''
print('コントラクトを呼び出します。中止するにはCtrl-Cを押してください。')

try:
    from time import sleep
    while True:
        result = c_func.call()
        print('ETH/USD: ', result)
        sleep(1)
except KeyboardInterrupt:
    print('終了します。')

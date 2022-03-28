import solcx
from pprint import pprint
import json
import os
import sys

if __name__ == '__main__':

    cname = os.getenv('CONTRACTNAME')
    if cname is None:
        print('環境変数CONTRACTNAMEを設定してください。')
        sys.exit(1)

    cname_lower = cname.lower()
    srcfile = cname_lower + '.sol'
    outbyte = cname + '.bytecode'
    outabi = cname + '.abi'

    print(srcfile, 'をコンパイルします。')
    # solc_ver = os.getenv('SOLC_VERSION')
    # if solc_ver is None:
    #     print('環境変数SOLC_VERSIONを設定してください。')
    #     sys.exit(1)

    resultdict = solcx.compile_files(
        [srcfile],
        output_values=['abi', 'bin'],
        base_path='node_modules'
    )

    print('コンパイルが完了しました。結果を保存します。')
    
    mycontract = resultdict[srcfile + ':' + cname]

    print('abi:', mycontract['abi'])
    print('bytecode:', mycontract['bin'])

    with open(outbyte, 'wt') as fp:
        fp.write(mycontract['bin'])
        print('バイトコードを', outbyte, 'に保存しました。')
   
    with open(outabi, 'wt') as fp:
        json.dump(mycontract['abi'], fp)
        print('ABIを', outabi, 'に保存しました。')


    print('compile.pyを終了します。')
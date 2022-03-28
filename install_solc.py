''' install_solc.py - 必要なバージョンのsolcをインストールする '''

import os
import sys
import solcx

if __name__ == '__main__':
    ver = os.getenv('SOLC_VERSION')

    if ver is None:
        print('環境変数SOLC_VERSIONを設定してください。')
        sys.exit(1)
    else:
        print('指定されたSOLCのバージョンは', ver, 'です。')

    existing = solcx.get_installed_solc_versions()
    installed = False
    for v in existing:
        if str(v) == ver:
            installed = True

    if installed is False:
        print('solc バージョン', ver, 'をインストールします。')
        solcx.install_solc(ver)
    elif installed is True:
        print('すでにインストールされているバージョンです。')

    print(__file__, 'を終了します。')
    sys.exit(0)

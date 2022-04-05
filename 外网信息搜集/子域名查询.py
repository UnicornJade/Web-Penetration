"""
#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
import socket
def main():
    '''
    1. 字典爆破
    2. 利用bing或第三方接口查询
    '''
    for zym in open('subnames_full.txt'):
        zym=zym.strip()
        subdomain=zym+'.xueersi.com'
        try:
            ip=socket.gethostbyname(subdomain)
            print(subdomain+' -- '+ip)
        except Exception as e:
            pass
    
    
if __name__ == '__main__':
    main()
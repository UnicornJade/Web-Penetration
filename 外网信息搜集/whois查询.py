"""
#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
import socket

def main():
    domain_name = 'www.baidu.com'
    print("##域名反查ip...")
    try:
        ip = socket.gethostbyname(domain_name)
        print('[+] %s 的ip地址：' % domain_name, ip)
    except:
        print('[!] 域名解析错误')
        print('[!] Exiting......')
        return
    whois_data = whois(domain_name)
    print(whois_data)
    
    pass
    
    
if __name__ == '__main__':
    main()
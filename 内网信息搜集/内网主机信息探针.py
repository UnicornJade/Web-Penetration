"""
#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
import nmap
'''
1. 原生ping探活
2. 原生利用icmp,tcp,udp等协议获取
3. 利用第三方模块库nmap等加载扫描
'''

def main():
    nmp=nmap.PortScanner()
    try:
        data=nmp.scan(hosts='',arguments='-T4 -F')
        print(nmp.all_hosts())
        print(nmp.csv())

    except Exception as e:
        pass

    
    
if __name__ == '__main__':
    main()
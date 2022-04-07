"""
#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
import socket
def main():
    '''
    1. 通过socket协议tcp、udp扫描
    2. 调用第三方masscan，nmap模块等扫描
    3. 调用系统工具脚本执行
    '''
    #1. tcp/udp扫描
    print('##端口扫描...')
    server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ports = {21, 22, 135, 443, 445, 80, 1433, 3306, 3389, 1521, 8000, 8080, 7002, 7001, 9090, 8089, 4848}
    for p in ports:
        con_res=server.connect_ex((ip,p))
        if con_res==0:
            print('[+] '+p+' | open ')
    
    pass
    
    
if __name__ == '__main__':
    main()
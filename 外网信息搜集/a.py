"""
#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
import socket,os,re
from whois import whois

ip='0.0.0.0'

def WHOIS(domain_name):
    """(一)域名反查ip/whois查询"""
    global ip
    print("##域名反查ip...")
    try:
        ip=socket.gethostbyname(domain_name)
        print('[+] %s 的ip地址：'%domain_name,ip)
    except:
        print('[!] 域名解析错误')
        print('[!] Exiting......')
        return
    whois_data=whois(domain_name)
    print(whois_data)
    """================================================================================================================================"""
    """(二)识别是否存在CDN"""
def CDN_Check(domain_name):
    ##1. nslookup返回ip解析数目判断(windows/linux通用命令)

    ###执行系统命令函数//[os.system只能打印不能操作数据(不可读取)]
    ###CDN_data=os.system('nslookup '+domain_name)
    print("##CDN服务判断...")
    cdn_data=os.popen('nslookup '+domain_name).read()
    ##ip正则匹配: re.findall(r"\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b",cdn_data)
    #通过判断nslookup返回数据中.的个数判断cdn，大于10就有cdn
    if(cdn_data.count('.')>10):
        print('[+] 存在CDN服务！！！')
    else:
        print('[+] 不存在CDN服务~')

    """================================================================================================================================"""
    """(三)端口扫描"""
def PORT_SCAN(ip):
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

def Sub_Domain(domain):
    '''
        1. 字典爆破
        2. 利用bing或第三方接口查询
    '''
    del_domain=domain.split('.')[0]
    re_domain=domain.lstrip(del_domain)
    #print(re_domain)
    for zym in open('subnames_full.txt'):
        zym = zym.strip()
        subdomain = zym + re_domain
        try:
            ip = socket.gethostbyname(subdomain)
            print(subdomain + ' -- ' + ip)
        except Exception as e:
            pass

def main():
    domain=input("[+] 请输入目标域名：")
    print("============\n* 功能模块:\n   1. WHOIS  2. CDN_Check 3. PORT_SCAN 4. Sub_Domain\n============")
    domain_only={'WHOIS','CDN_Check','Sub_Domain'}
    func=input('[+] 请输入想要使用的功能\n$> ')
    if func in domain_only:
        eval(func)(domain)
    else:
        ip2=input('[*] 请输入目标ip: ')
        eval(func)(ip2)
    print('\n\n> > > > > > < < < < < < ')
    print('<@> 程序执行完毕咯~')

    
    
if __name__ == '__main__':
    main()
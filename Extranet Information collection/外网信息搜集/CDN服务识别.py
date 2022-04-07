"""
#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
import os
def main():
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
    
    pass
    
    
if __name__ == '__main__':
    main()
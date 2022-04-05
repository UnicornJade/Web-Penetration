"""
#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
import mmh3
import requests
def main():
    resp=requests.get('+')

    favicon=resp.content.encode('base64')
    hash=mmh3.hash(favicon)
    print('http.favicon.hash:'+str(hash))

    pass
    
    
if __name__ == '__main__':
    main()
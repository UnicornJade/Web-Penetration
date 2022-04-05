"""
#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
import requests,json,time
def sqlmapapi(url):
    data = {
        'url': url #'http://192.168.183.131/sqli-labs/Less-4/?id=1'
    }
    headers = {
        'Content-Type': 'application/json'
    }

    task_new_url = 'http://127.0.0.1:8775/task/new'
    resp = requests.get(task_new_url)
    # print(resp.json()) #{'taskid': '49d9df8c73af91b9', 'success': True}
    task_id = resp.json()['taskid']
    if 'success' in resp.content.decode('utf-8'):
        print('[+] Sqlmapapi Task Create Successfully...')
        task_set_url = 'http://127.0.0.1:8775/option/' + task_id + '/set'
        task_set_resp = requests.post(task_set_url, data=json.dumps(data), headers=headers)
        if 'success' in task_set_resp.content.decode('utf-8'):
            print('[+] Sqlmapapi Task Set Successfully...')
            task_start_url = 'http://127.0.0.1:8775/scan/' + task_id + '/start'
            task_start_resp = requests.post(task_start_url, data=json.dumps(data), headers=headers)
            if 'success' in task_start_resp.content.decode('utf-8'):
                print('[+] Sqlmapapi Task Start Successfully...')
                print('<--Waiting--> Sqlmapapi Task Scan Is Running......')
                while 1:
                    task_status_url = 'http://127.0.0.1:8775/scan/' + task_id + '/status'
                    task_status_resp = requests.get(task_status_url)
                    if 'running' in task_status_resp.content.decode('utf-8'):
                        time.sleep(3)
                        continue
                    else:
                        print('[ * ] Sqlmapapi Task Scan Finished!\n= = = = = = = = = = = =')
                        task_data_url = 'http://127.0.0.1:8775/scan/' + task_id + '/data'
                        task_data_resp = requests.get(task_data_url)
                        scan_data=task_data_resp.content.decode('utf-8')
                        # print(task_data_resp.content.decode('utf-8'))
                        if 'success' in task_data_resp.content.decode('utf-8'):
                            with open('E:\Py-Pro\Web-Penetration\Tool expansion\Scan Data\Scan_Data.txt', 'a+') as f:
                                f.write(url + '\n')
                                f.write(scan_data + '\n')
                                f.write('==========python sqlmapapi ==========' + '\n')
                                f.close()
                            print('[ * ] Data Of  '+url+" is loaded")
                            # print('delete taskid')
                            scan_deltask_url = 'http://127.0.0.1:8775/task/' + task_id + '/delete'
                            scan_deltask = requests.get(scan_deltask_url)
                            if 'success' in scan_deltask.content.decode('utf-8'):
                                print('delete taskid success')
                        break




def main():
    url_file=open('urls.txt','r')
    for url in url_file.readlines():
        url=url.strip()
        sqlmapapi(url)
    
    pass
    
    
if __name__ == '__main__':
    main()
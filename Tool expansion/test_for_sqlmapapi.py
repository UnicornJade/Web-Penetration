"""
#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
import requests,json

def main():
    #1.创建任务id
    task_new_url ='http://127.0.0.1:8775/task/new'
    resp = requests.get(task_new_url)
    # print(resp.json()) #{'taskid': '49d9df8c73af91b9', 'success': True}
    task_id=resp.json()['taskid']

    #2.设置任务id的配置信息（扫描信息）
    data={
        'url': 'http://192.168.183.131/sqli-labs/Less-4/?id=1'
    }
    headers={
        'Content-Type': 'application/json'
    }
    task_set_url='http://127.0.0.1:8775/option/'+task_id+'/set'
    task_set_resp=requests.post(task_set_url,data=json.dumps(data),headers=headers)
    #print(task_set_resp.content.decode('utf-8'))

    #3.启动对应id的扫描任务
    task_start_url = 'http://127.0.0.1:8775/scan/'+task_id+'/start'
    task_start_resp=requests.post(task_start_url,data=json.dumps(data),headers=headers)
    #4.获取对应id的扫描状态
    task_status_url = 'http://127.0.0.1:8775/scan/'+task_id+'/status'
    task_status_resp=requests.get(task_status_url)

    #5.获取结果
    task_data_url = 'http://127.0.0.1:8775/scan/' + task_id + '/data'
    task_data_resp = requests.get(task_data_url)

    #6.删除task_id
    scan_deltask_url = 'http://127.0.0.1:8775/task/' + task_id + '/delete'
    scan_deltask = requests.get(scan_deltask_url)
    pass
    
    
if __name__ == '__main__':
    main()
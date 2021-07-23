import paramiko
import time
import sys
import re

def ssh_cmd(ip,username,password,cmd_list,verbose=True):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip,port=22,username=username,password=password,timeout=5,compress=True)
    chan = ssh.invoke_shell()
    time.sleep(1)
    x = chan.recv(2048).decode()
    for cmd in cmd_list:
        chan.send(cmd.encode())
        chan.send(b'\n')
        time.sleep(2)
        x = chan.recv(40960).decode()
        if verbose:
            return x.split('\n')[-3],x.split('\n')[-4]
    chan.close()
    ssh.close()


if __name__ == '__main__':
    ssh = ssh_cmd('1.1.1.200', 'cisco', 'cisco', ['sho flow monitor name qytang-monitor cache format table'], )
    # ret = re.match(
    #     r'\n(\w+\s+\w+\s+\w+)(\d+)\n\w+\s+(\w+\s+\w)(\d+)\n(\w+\s+\w+-\w+)\s+(\d+)',
    #     ssh)
    netflow_list = []
    for i in ssh:
        ret = re.match(r'(\w+\s+\w+)\s+(\d{3,5})', i).groups()
        netflow_list.append(ret)
    print(netflow_list)

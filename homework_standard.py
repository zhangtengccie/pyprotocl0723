import paramiko
import re
from pyprotocl0723.netflow import mat_bing

def ssh_cli(ip, username, password, cmd):
    try:
        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, port=22, username=username, password=password, timeout=5, compress=True)
        stdin, stdout, stderr = ssh.exec_command(cmd)
        x = stdout.read().decode()
        return x
    except Exception as e:
        print('%stErrorn %s'%(ip,e))
def get_netflow_app():
    show_result = ssh_cli('1.1.1.200','cisco','cisco','sho flow monitor name qytang-monitor cache format table ')
    app_name_list = []
    app_bytes_list = []
    for line in show_result.strip().split('\n'):
        app_bytes = re.match(r'^((port|layer7) [a-z]+)\s+(\d+)',line)
        if app_bytes:
            app_name_list.append(app_bytes.groups()[0])
            app_bytes_list.append(app_bytes.groups()[2])
    mat_bing(app_bytes_list,app_name_list)


if __name__ == '__main__':
    get_netflow_app()
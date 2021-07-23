import matplotlib
from matplotlib import pyplot as plt
from ssh import ssh_cmd
import re

print(matplotlib.matplotlib_fname())
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.family'] = 'sans-serif'


def mat_bing(size_list, name_list):
    plt.figure(figsize=(6, 6))
    patches, label_text, percent_test = plt.pie(size_list,
                                                labels=name_list,
                                                labeldistance=1.1,
                                                autopct='%3.1f%%',
                                                shadow=False,
                                                startangle=90,
                                                pctdistance=0.6)
    for l in label_text:
        l.set_size = 30
    for p in percent_test:
        l.set_size = 20
    plt.axis('equal')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    ssh = ssh_cmd('1.1.1.200', 'cisco', 'cisco', ['sho flow monitor name qytang-monitor cache format table'], )
    netflow_list = []
    for i in ssh:
        ret = re.match(r'(\w+\s+\w+)\s+(\d{3,5})', i).groups()
        netflow_list.append(ret)

    counters = [netflow_list[0][1],netflow_list[1][1]]
    protocols = [netflow_list[0][0],netflow_list[1][0]]
    mat_bing(counters, protocols)

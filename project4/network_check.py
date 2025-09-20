# network_check.py
# 模拟网络诊断脚本

import os

def ping_host(host):
    response = os.system(f"ping -c 2 {host}")
    if response == 0:
        print(f"{host} is reachable")
    else:
        print(f"{host} is NOT reachable")

def main():
    hosts = ["192.168.3.1", "8.8.8.8"]
    for host in hosts:
        ping_host(host)

if __name__ == "__main__":
    main()

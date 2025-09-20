# monitor.py
# 模拟远程服务器监控

def get_cpu_usage():
    return "CPU Usage: 35%"

def get_memory_usage():
    return "Memory Usage: 60%"

def get_disk_usage():
    return "Disk Usage: 120GB/500GB"

def main():
    print(get_cpu_usage())
    print(get_memory_usage())
    print(get_disk_usage())

if __name__ == "__main__":
    main()

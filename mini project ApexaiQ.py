import psutil

def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu_usage}%")

def check_memory_usage():
    memory_info = psutil.virtual_memory()
    print(f"Total Memory: {memory_info.total / (1024 ** 3):.2f} GB")
    print(f"Used Memory: {memory_info.used / (1024 ** 3):.2f} GB")
    print(f"Memory Usage: {memory_info.percent}%")
def check_disk_space():
    disk_usage = psutil.disk_usage('/')
    print(f"Total Disk Space: {disk_usage.total / (1024 ** 3):.2f} GB")
    print(f"Used Disk Space: {disk_usage.used / (1024 ** 3):.2f} GB")
    print(f"Disk Usage: {disk_usage.percent}%")

def main():
    print("Checking System Health:")
    check_cpu_usage()
    check_memory_usage()
    check_disk_space()

main()
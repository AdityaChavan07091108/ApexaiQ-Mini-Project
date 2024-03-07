import psutil
import time
import pandas as pd
cpu_usage=[]
memory_total=[]
memory_used=[]
memory_percent=[]
disk_total=[]
disk_used=[]
disk_percent=[]

def check_cpu_usage():
    cpu_usage_value = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu_usage_value}%")
    cpu_usage.append(cpu_usage_value)

def check_memory_usage():
    memory_info = psutil.virtual_memory()
    total = f"{memory_info.total / (1024 ** 3):.2f} "
    print(f"Total Memory: {total} GB")
    memory_total.append(total)
    
    used = f"{memory_info.used / (1024 ** 3):.2f} "
    print(f"Used Memory: {used} GB")
    memory_used.append(used)
    
    percent=memory_info.percent
    print(f"Memory Usage: {percent}%")
    memory_percent.append(percent)
    
def check_disk_space():
    disk_usage = psutil.disk_usage('/')
    total=f"{disk_usage.total / (1024 ** 3):.2f} "
    print(f"Total Disk Space: {total} GB")
    disk_total.append(total)
    
    used=f"{disk_usage.used / (1024 ** 3):.2f} "
    print(f"Used Disk Space: {used} GB")
    disk_used.append(used)
    
    percent=disk_usage.percent
    print(f"Disk Usage: {percent}%")
    disk_percent.append(percent)

def main():
    print("Checking System Health:")
    for _ in range(180):  # Run for 180 seconds
        check_cpu_usage()
        check_memory_usage()
        check_disk_space()
        time.sleep(3)  # Sleep for 3 second between each check
    final={
        "CPU Usage": cpu_usage,
        "Total Memory": memory_total,
        "Used Memory": memory_used,
        "Memory Percentage":memory_percent,
        "Total Disk Space":disk_total,
        "Disk Space Used":disk_used,
        "Disk Usage Percentage":disk_percent        
    }
    df = pd.DataFrame(final)
    df.to_csv('proj_system_data.csv', index=False)
    print("Ho gyi file save!😁")      
main()

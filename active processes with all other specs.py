import psutil
import csv

def get_running_apps_info():
    app_info = []
    for proc in psutil.process_iter(['name', 'memory_percent', 'cpu_percent', 'pid']):
        try:
            if proc.info['pid'] == 0:
                continue  # Skip the System Idle Process
            
            if proc.info['name'] in ('System Idle Process', 'System'):
                continue  # Skip system processes
            
            if not proc.info.get('name'):
                continue  # Skip processes with no name
            
            if proc.info['memory_percent'] == 0 and proc.info['cpu_percent'] == 0:
                continue  # Skip processes with no CPU or memory usage
            
            # Check if the process has a visible window
            if not proc.info.get('pid'):
                continue  # Skip processes with no pid
            
            app_name = proc.info['name']
            memory_usage = proc.info['memory_percent']
            cpu_usage = proc.info['cpu_percent']
            
            app_info.append({'Name': app_name, 'Memory Usage (%)': memory_usage, 
                             'CPU Usage (%)': cpu_usage})
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return app_info

def write_to_csv(app_info):
    with open('app_infov1.csv', mode='w', newline='') as file:
        fieldnames = ['Name', 'Memory Usage (%)', 'CPU Usage (%)']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        writer.writeheader()
        for app in app_info:
            writer.writerow(app)

if __name__ == "__main__":
    running_apps_info = get_running_apps_info()
    write_to_csv(running_apps_info)

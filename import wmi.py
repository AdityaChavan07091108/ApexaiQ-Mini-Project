import psutil

def get_running_apps():
    apps = set()
    for proc in psutil.process_iter(['name', 'pid', 'create_time']):
        if proc.info['name']:
            apps.add(proc.info['name'])
    return apps

if __name__ == "__main__":
    running_apps = get_running_apps()
    print("Running Applications:")
    for app in running_apps:
        print(app)

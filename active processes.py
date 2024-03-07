import psutil

# Get a list of all running processes
running_processes = psutil.process_iter()

# Iterate over the list of processes and fetch information
for process in running_processes:
    try:
        # Get process details
        process_id = process.pid
        process_name = process.name()
        process_status = process.status()
        process_memory_usage = process.memory_info().rss  # Resident Set Size (RSS) in bytes

        # Print process details
        print(f"Process ID: {process_id}")
        print(f"Process Name: {process_name}")
        print(f"Process Status: {process_status}")
        print(f"Memory Usage: {process_memory_usage} bytes")
        print("-" * 50)  # Separator
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        # Handle exceptions for processes that cannot be accessed
        pass

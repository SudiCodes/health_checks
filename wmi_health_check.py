import wmi

def get_remote_system_info(remote_host, username, password):
    # Connect to the remote machine's WMI service
    c = wmi.WMI(remote_host, user=username, password=password)

    # Get the hostname of the remote machine
    for system in c.Win32_ComputerSystem():
        hostname = system.Name

    # Get CPU usage of the remote machine
    for cpu in c.Win32_PerfFormattedData_PerfOS_Processor():
        cpu_usage = cpu.PercentProcessorTime

    # Get Total Physical Memory
    for os in c.Win32_OperatingSystem():
        total_physical_memory = int(os.TotalVisibleMemorySize)

    # Get Free Physical Memory
    for os in c.Win32_OperatingSystem():
        free_physical_memory = int(os.FreePhysicalMemory)

    # Calculate used physical memory
    used_physical_memory = total_physical_memory - free_physical_memory

    # Calculate RAM usage percentage
    ram_usage = (used_physical_memory / total_physical_memory) * 100

    # Get Total Disk Space
    for disk in c.Win32_LogicalDisk(DriveType=3):
        total_disk_space = int(disk.Size)

    # Get Free Disk Space
    for disk in c.Win32_LogicalDisk(DriveType=3):
        free_disk_space = int(disk.FreeSpace)

    # Calculate used disk space
    used_disk_space = total_disk_space - free_disk_space

    # Calculate disk usage percentage
    disk_usage = (used_disk_space / total_disk_space) * 100

    return hostname, cpu_usage, ram_usage, disk_usage

if __name__ == "__main__":
    # remote_host = "10.10.11.50"
    # username = "Administrator"
    # password = "sm_passwd"

    
    
    hostname, cpu_usage, ram_usage, disk_usage = get_remote_system_info(remote_host, username, password)
    print("Hostname:", hostname)
    print("CPU Usage:", cpu_usage, "%")
    print("RAM Usage:", ram_usage, "%")
    print("Disk Usage:", disk_usage, "%")

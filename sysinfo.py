import os
import datetime

#command = "systeminfo | find \"System Boot Time\""
#command = "powershell Get-Date"

def show_current_time():
    return datetime.datetime.now()
today = show_current_time()

print("Current Date and Time: ", today)
    

def check_cpu_usage(command):    # first define a function
    print(os.system(command))                    
check_cpu_usage("wmic cpu get loadpercentage")   # call the function with command as argument


def check_date(command):
    print(os.system(command))
check_date("powershell Get-Date")


def check_memory_usage(command):
    print(os.system(command))
check_memory_usage("wmic OS get FreePhysicalMemory,TotalVisibleMemorySize /Value")


def check_ram_usage(command):
    print(os.system(command))
check_ram_usage("wmic OS get FreePhysicalMemory,TotalVisibleMemorySize /Value")

def check_disk_usage(command):
    return os.system(command)
check_disk_usage("wmic logicaldisk get size,freespace,caption")
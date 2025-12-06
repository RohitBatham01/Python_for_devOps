import os # importing os module to interact with the operating system

print(os.system('df -h'))  # executing a system command to display disk space usage in human-readable format   (This is for linux or macOS)

print(os.system('wmic logicaldisk get size,freespace,caption'))  # executing a system command to display disk space usage in Windows

print(os.system('systeminfo'))  # executing a system command to display system information for WIndows 
print(os.system('systeminfo | find "System Boot Time"'))  # executing a system command to display system information for WIndows 


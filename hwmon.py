import psutil

print(psutil.cpu_times())
print(psutil.virtual_memory(), psutil.swap_memory())


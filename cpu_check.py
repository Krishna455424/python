import psutil
cpu = psutil.cpu_percent(interval=1)
print(cpu)
if (cpu>80):
    print("high cpu usage")
else:
    print("Normal usage")

import psutil

def check_cpu_usage():
    cpu_threshold = int(input("Enter CPU Threshold \n"))
    current_cpu_usage = psutil.cpu_percent(interval=1)

    if current_cpu_usage > cpu_threshold:
        print ("High CPU Usage :", current_cpu_usage)

    else:
        print ("CPU Usage is under threshold:", current_cpu_usage)


check_cpu_usage()
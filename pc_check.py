#!/user/bin/env python3

import shutil
import psutil

# Check percentage of free space and return True if more then 20% space free
def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20

# Check percentage of CPu usage every 1 SECOND and return True if less then 75%
def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage < 75

if not check_disk_usage("/") or not check_cpu_usage():
    print("ERROR!")
else:
    print("EVERYTHING IS OK")

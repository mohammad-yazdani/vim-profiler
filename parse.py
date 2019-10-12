#!/usr/bin/python

import subprocess

LOG_FILE="tmp_vim_profiling.log"

# Run vim startup profiling and save it to `LOG_FILE`
p = subprocess.Popen(["vim", "--startuptime", LOG_FILE, "+q"])
p.communicate()

# Read lines from log file
log_dump = open(LOG_FILE, 'r')

# Clean file log
p = subprocess.Popen(["rm", LOG_FILE])
p.communicate()

# Parse start times of sourcings to a float array
times = []
for line in log_dump:
    if "sourcing" in line:
        words = line.split()
        try:
            times.append([words[4], float(words[1])])
        except ValueError:
            continue

# Sort times
def sort_time_elapsed(elem):
    return elem[1]
times.sort(key=sort_time_elapsed)

# Pretty print
max_src_len = 0
for time in times:
    max_src_len = max(max_src_len, len(time[0]))
for time in times:
    print(("{:<" + str(max_src_len) + "s}{:>25.2f}").format(time[0], time[1]))


#!/usr/bin/env python3

#
# Periodically launches a new instance of the given program.
# Inputs:
#  - interval (seconds)
#  - maximum number of instances
#  - CSV output filename
#  - program with arguments (in quotes): ex: "glxgears -geometry 1280x720 -csv /tmp/frametimes_%i.csv"
#       - "%i" in this string is replaced with an incrementing id
#

import time
import sys
from subprocess import Popen

processes = []


def launch_processes(sleep_time_sec, num_instances, csv_filename, proc_name_args):
    csv = open(csv_filename, 'w')
    for n in range(0, num_instances):
        proc_name_args_expanded = [x.replace("%i", str(n)) for x in proc_name_args]
        p = Popen(proc_name_args_expanded)
        launch_time_ms = round((time.time() * 1000))
        print(f"{launch_time_ms},{n}", file=csv)
        processes.append(p)
        csv.flush()
        try:
            time.sleep(sleep_time_sec)
        except KeyboardInterrupt:
            print("END")
            exit(0)


def usage():
    print(f"{sys.argv[0]} <interval in seconds> <max instances> <CSV filename> <proc name with args in quotes>")


def main():
    if len(sys.argv) < 5:
        usage()
        exit(-1)

    interval_sec = int(sys.argv[1])
    num_instances = int(sys.argv[2])
    csv_filename = sys.argv[3]
    proc_name_args = sys.argv[4].split()
    print(f"# inverval_sec={interval_sec}, num_instances={num_instances}), csv_filename={csv_filename}")
    print(f"# proc_name_args={proc_name_args}")

    launch_processes(interval_sec, num_instances, csv_filename, proc_name_args)
    print(f"Done launching {num_instances} instances. Killing them now ...")

    for p in processes:
        print(f"Killing {p.pid} ...")
        p.kill()


main()

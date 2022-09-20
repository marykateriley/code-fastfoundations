import multiprocessing
import os

import sys


def calculate_geometric_series(a, r, n=10):
    print(f"child process: {os.getpid() = }")
    if r == 1:
        print(f"s_{n}({a = }, {r = } = {a * (n + 1)}")
    else:
        print(f"s_{n}({a = }, {r = } = {a * (1 - r ** (n + 1)) / (1 - r)}")


def main():
    print(f"parent process: {os.getpid() = }")
    process = multiprocessing.Process(
        name='calculate_geometric_series',
        target=calculate_geometric_series, # name of the callable to run as a seperate process
        args=(2, 0.333333333, 1000) # sequence of arguments that the function will take
    )
    process.daemon = True # to run in the background. daemon is a process that is detached from all terminals - isloated from eveything else. useful to log its output to a log file as it doesn't have a terminal etc
    process.start() # process will wait until we call start. After we call start, python will create a new process
    process.join()  # if daemon then no need to join
    return 0


if __name__ == "__main__":
    sys.exit(main())

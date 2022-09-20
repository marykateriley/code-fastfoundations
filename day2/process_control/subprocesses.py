""""""
import os
import shlex
import subprocess
import sys
import time


def simplest_way():
    process = subprocess.run( # subprocess talks to the OS - is telling the OS that it should run sleep 10 (sleep for 10 seconds)
        shlex.split("sleep 10") # waits 10 seconds before printing the command. shlex =shell lexer, A lexer is a toll that is able to pass astring, and returns the parts of the string that has different functions/roles. Ensure's all quotes are used correctly
    ) # python immediately started sleep at the end of this call - sleep for 10 seconds just to "sleep 10"
    print(f"{process = }")
    print(f"{process.args = }") # shows arguments that have been passed
    print(f"{process.returncode = }")
    print(f"{process.stdout = }")
    print(f"{process.stderr = }")


def create_subprocess():
    # https://docs.python.org/3/library/subprocess.html#popen-constructor
    print(f"{os.getpid() = }")  # the process id for this module's process
    process = subprocess.Popen(
        shlex.split(
            "python /Users/mary-kateriley/PycharmProjects/code-fastfoundations/day2/process_control/simple_task.py"
        ),
        stdin=subprocess.PIPE,  # necessary to communicate the input value
        stdout=subprocess.PIPE,  # necessary to retrieve the output values
        stderr=subprocess.PIPE  # ditto
    )
    print(f"{process.pid = }")
    stdout, stderr = process.communicate(input=b"2\n0.3333333\n10\n")  # send input; receive output; bytes
    print(f"{process = }")
    print(f"{stdout = }")
    print(f"{stderr = }")
    print(f"{process.returncode = } 👍")  # exit code


def stop_subprocess():
    print(f"{os.getpid() = }")
    process = subprocess.Popen(
        shlex.split("sleep 1000")
    )
    print(f"{process.pid = }")
    print(f"Parent will now sleep for 5s...")
    time.sleep(5) # the parent is sleeping, but this will happen after 5 seconds
    print(f"Hmm... This is taking too long!")
    print(f"{process.poll() = } (None = 'still running')")
    time.sleep(5)
    print(f"That's it! I've had it!")
    process.kill()
    stdout, stderr = process.communicate()
    print(f"{stdout = }")
    print(f"{stderr = }")
    print(f"{process.returncode = } 😵")  # -9 is the exit code (how you kill a process)

#TASK
def find_paradoxical(): ## check solutions for answer
    process = subprocess.Popen(
        shlex.split(
        "find .. - name ‘*paradoxical. *’ -type"
        ),
        stdin=subprocess.PIPE,  # necessary to communicate the input value
        stdout=subprocess.PIPE,  # necessary to retrieve the output values
        stderr=subprocess.PIPE
    )
    print(f"{process.pid = }")
#find_paradoxical

def main():
    # simplest_way()
    # create_subprocess()
    # stop_subprocess()
    return 0 # this reports back to the operating system to ensure everything is ok


if __name__ == '__main__':
    sys.exit(main())

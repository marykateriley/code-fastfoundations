import sys


def plain_while():
    i = 0
    while i < 10:
        print(f"{i = }")
        i += 1 # if we don't incremate by 1, then the loop will go on forever


def complex_while():
    from my_functions import calculate_geometric_series

    while True:  # loop forever!
        a = int(input("a: "))
        r = float(input("r: "))
        n = int(input("n: "))
        s_n = calculate_geometric_series(a, r, n)
        print(f"{s_n = }")
        quit_ = input("to quit enter 'q': ")  # why do we use 'quit_' instead of 'quit'
        if quit_ == 'q': # quit is an internal function, that's why we use quit_
            break # exits from the loop

#TASK
def reverse_while():
    i = 9
    while i > -1:
        print(f"{i = }")
        i -= 1
#reverse_while()

def sum_1000(): ## need to fix this, answer is giving 1001
    i = -12
    sum_ = 0
    while True: # loop forever as we don't know where it will end
        if sum_ > 1000:
            sum_ -= i # without this, it would print out the value above 1000 that it reaches. so this takes away the last value of i, which is thje first value before 1000
            break
        sum_ += i
        i += 1
    print(f"{sum_ = }")
#sum_1000()

def loop_over_file():
    with open("paradoxical.txt") as f:
        while line := f.readline():
            print(f"{line = }")


def main():
    # plain_while()
    # complex_while()
    #loop_over_file()
    return 0


if __name__ == '__main__':
    sys.exit(main())

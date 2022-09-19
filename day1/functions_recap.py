import sys

## refer to slide 26 on day 1 presentation. This is the equation
def calculate_geometric_series(a, r, n=10): ## n is a keyword arugument
    """Calculate the sum of a geometric series"""
    if r == 1: ## this is a conditional construct (comparision due to ==)
        return a * (n + 1)
    return a * (1 - r ** (n + 1)) / (1 - r)

def get_max(a_list): ## not 'list' as 'list' is already a function
    maximum = None
    first = False
    for value in a_list:
        if not first:
            maximum = value
            first = True
        if value > maximum:
            maximum = value
    return maximum


def main():
    # a = int(input("a: "))
    # r = float(input("r: "))
    # n = int(input("n: "))
    # print(f"s_n = {calculate_geometric_series(a, r, n)}")
    my_list=[1, 7, 9, 42]
    my_max=get_max(my_list)
    print(f"{my_max}")
    return 0




if __name__ == "__main__":
    sys.exit(main())

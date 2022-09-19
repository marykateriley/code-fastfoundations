import random  # this is the random library
import sys


def double_number(n):
    return 2 * n


def using_map():
    """Double the given number"""
    random_numbers = random.choices(range(200), k=10)
    print(f"{random_numbers = }")  # f embeds list into the string
    print(f"{map(double_number, random_numbers) = }")


def using_map_and_lambda():
    """Using map with a lambda"""
    random_numbers = random.choices(range(200), k=10)
    print(f"{random_numbers = }")
    print(f"{map(lambda r: 2 * r, random_numbers) = }")


def using_filter():
    """Filter out words that are in the wrong case"""
    words = ["shock", "brink", "limited", "admission", "demonstration", "alive", "pen", "reactor", "ban", "sentence", ]
    print(f"{words = }")
    print(f"{filter(lambda w: len(w) > 7, words) = }")
    print(f"{list(filter(lambda w: len(w) > 7, words)) = }")  # only shows filtered list


def square_dict(a_dict):
    output_dict = dict()
    for key, value in a_dict.items(): # .items gives two values as a tuple
        print(f"{key} -> {value ** 2}") # unpacks tuple into key and value
    return


def main():
    # using_map()/
    # using_map_and_lambda()
    # using_filter()
    my_dict = {'nine': 9, 'ten': 10, 'eleven': 11}
    square_dict(my_dict)
    return 0


if __name__ == '__main__':
    sys.exit(main())

import sys


def opening_and_closing_files():
    f = open("think_different.txt")  # details: https://docs.python.org/3/library/functions.html#open, f is called a file handle
    quote = f.read() #will read everything
    print(f"{quote = }")
    # try and read again
    quote_again = f.read()
    print(f"{quote_again = }") # this is empty to show that there is nothing left in the file
    # don't forget! otherwise you will exhaust the file handles
    f.close()


def reading_file_contents():
    with open("think_different.txt") as f: #as gives the name to f i.e. open file in read only as f
        # read everything
        print(f"{f.read()[:30]}...") # [:30] slices the first 30 characters, from 0 to 29 (excludes 30)

    print(f"{f = }")
    print(f"{f.closed = }") # files have an attribute called closed
    # print(f"{f.read() = }") # raises ValueError: I/O operation on closed file.

    with open("think_different.txt") as f:
        # read one line at a time; up to the \n
        print(f"{ f.readline() = }")

    with open("think_different.txt") as f:
        # list of all lines
        print(f"{ f.readlines() = }")


def navigating_files():
    with open("butterfly.txt") as f:
        # first let's read everything
        print(f"{f.read() = }")
        # try and read again... nothing
        print(f"{f.read() = }")
        # where are we?
        print(f"{f.tell() = }")
        # let's go back to the beginning
        print(f"{f.seek(0) = }")
        # ten steps forward....
        print(f"{f.seek(10) = }")
        # perfect!
        print(f"{f.read() = }")

#TASK
def iterating_over_file_contents():
    with open("think_different.txt") as f:
        for row in f:
            print(row) # this prints each line individually, as the print function creates a new line. Use strip (below)
#iterating_over_file_contents()

def iterating_over_file_contents_strip():
    with open("think_different.txt") as f:
        for row in f:
            print(row.strip()) # does not print a new line between each line of text
#iterating_over_file_contents_strip()

def reading_wagata():
    with open("wagata.txt", encoding="utf-32") as f:
        print(f.read())
#reading_wagata()

def print_number_of_rows(filename, lines=10):
    with open(filename) as f:
        # slicing
        lines_read = f.readlines()[:lines]
        print(lines_read)
        print(len(lines_read))
#print_number_of_rows("paradoxical.txt")



def working_with_paths():
    import pathlib
    my_path = pathlib.Path(".")  # bash: the current directory
    print(f"{type(my_path)}")  # what is the type
    print(f"{my_path.owner() = }")
    print(f"{my_path.parent = }")
    print(f"{my_path.name = }") # no file name as it's a directory
    print(f"{my_path.parent.absolute() = }")
    print(f"{my_path.parents = }")
    file_path = my_path / 'our_deepest_fear.txt.gz'  # paths works with the / operator
    print(f"{my_path / 'our_deepest_fear.txt.gz' = }")
    print(f"{file_path.absolute() = }")
    print(f"{file_path.name = }")
    print(f"{file_path.suffix = }")
    print(f"{file_path.suffixes = }")
    print(f"{file_path.stem = }") # excludes the last suffix


def testing_paths():
    import pathlib
    my_path = pathlib.Path("..")  # the parent directory
    print(f"{my_path.exists() = }")
    print(f"{my_path.is_dir() = }")
    print(f"{my_path.is_file() = }")
    print(f"{my_path.is_absolute() = }") # wasn't specified absolutely
    print(f"{my_path.is_relative_to('/Users/paulkorir/') = }") # asking if it is relative to this file? no.
    print(f"{my_path.is_relative_to('.') = }") # . means current foler and .. means parent folder


def useful_path_operations():
    import pathlib
    my_path = pathlib.Path("dir1/dir3/dir4/einstein.txt") # uses formatting minilanguage, is within the 'day2' file
    with my_path.open() as f: # do not have to specify file again as it is assumed
        print(f.read())
    my_path = pathlib.Path("dir1/dir3/dir4/einstein.txt")  # ~ = user dir
    # with my_path.open() as f: # raises an exception
    #     print(f.read())
    with my_path.expanduser().open() as f:  # need to expand user first
        print(f.read())
    my_path = pathlib.Path(".") # the ~ refers to home directory, but the we specified that . is the parent
    print(f"{my_path.glob('*') = }")  # globbing; just like on the bash terminal
    print(f"{'GLOBBING'}") # globbing is not the same as regular expression as it is on a path, not a string
    for path_object in my_path.glob('*'):
        print(f"\t* {path_object.name:<30} ==> {path_object.parent}")
    print(f"{'GLOBBING & SORTING'}")
    for python_modules in sorted(my_path.glob('*.py')):  # sortable!
        print(f"\t* {python_modules.name}")
    print(f"{'RECURSIVE GLOBBING'}") # allows us to get all contents in all folders and sub folders from the parent
    for path_object in my_path.rglob('**/*'):  # recursive globbing
        print(f"\t* {path_object.name:<30} ==> {path_object.parent}")

#TASK
def reading_socrates():
    import pathlib
    my_path = pathlib.Path("dir1/dir2/socrates.txt")
    with open(my_path) as f:
        print(f.read())
#reading_socrates()

def read_hidden():
    import pathlib
    my_path = pathlib.Path("~/") # glob for all hidden files in user dir
    print(f"{my_path =}")
    for fn in my_path.expanduser().glob("*"):
        print(fn)
#read_hidden()
def main():
    # opening_and_closing_files()
    # reading_file_contents()
    # iterating_over_file_contents()
    # navigating_files()
    # working_with_paths()
    # testing_paths()
    # useful_path_operations()
    return 0


if __name__ == '__main__':
    sys.exit(main())

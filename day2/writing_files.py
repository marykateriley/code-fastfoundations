import sys
import re


def writing_to_text_files():
    with open("my_fancy_file.txt", 'w') as f:
        f.write("1")  # no newline at the end
        f.write("2")  # no newline at the end
        f.write("3")  # no newline at the end
        f.write("4\n")  # now we add a new line
        f.write("5\n")  # again # check this by clicking my_fancy_file on the left
    with open("my_fancy_file.txt") as f:
        print(f"{f.read() = }") # reads everything as a string
    lines_of_text = [
        "Knowledge is power.\n",
        "Power to do evil... or power to do good.\n",
        "Power itself is not evil.\n",
        "So knowledge itself is not evil.\n",
        "― Veronica Roth, Allegiant\n", # adding \n puts each text in a new line, or use lamda when reading lines
    ]
    with open("power_quote.txt", 'w') as f:
        f.writelines(lines_of_text) # takes a list, only reads it as one line
        # f.writelines(map(lamda s: s + '\n', lines_of_text)) ALT way to add a new line
    with open("power_quote.txt") as f:
        print(f.readlines())


def creating_and_modifying_paths(): # using formatting minilanguage with a variable to specify the width of column
    import pathlib
    import datetime
    my_path = pathlib.Path("dir7/new_file.txt")  # a non-existent path
    col1 = 80
    print(f"{str(my_path.absolute()):{col1}}: {my_path.exists() = }")
    # with my_path.open('w') as f: # FileNotFoundError
    #     print(f"{datetime.datetime.now() = }\n", file=f) # another way to write to a file
    my_path.parent.mkdir()  # need to create the parent first, this literally creates the file dir7 (will appear on the left)
    print(f"{str(my_path.parent.absolute()):{col1}}: {my_path.parent.exists() = }")
    with my_path.open('w') as f:  # write
        print(f"{datetime.datetime.now() = }\n", file=f)  # another way to write to a file
    print(f"{str(my_path.absolute()):{col1}}: {my_path.exists() = }")
    # my_path.parent.rmdir() # FileExistsError #rmdir only removes empty directories
    my_path.unlink() # deletes by using the system call
    print(f"{str(my_path.absolute()):{col1}}: {my_path.exists() = }")
    my_path.parent.rmdir()
    print(f"{str(my_path.parent.absolute()):{col1}}: {my_path.parent.exists() = }")


def parsing_text_files():
    with open("Homo_sapiens.GRCh38.107.abinitio.gtf") as f:
        for row in f:  # files are iterators
            print(row.strip())  # remove trailing \n (strip removes white space)
    with open("Homo_sapiens.GRCh38.107.abinitio.gtf") as f:
        for row in f:
            cols = row.strip().split("\t") # splits into a list
            print(cols)
            # always need to read, loop through, strip new line characters and then split
            # most data in bioinformatics is comma delimited and tab delimited and will need to use this method

#TASK

def new_directory():
    import pathlib
    new_dir = pathlib.Path("dir1/dir3/dir5/new_file.txt")
    new_dir.parent.mkdir()
    with open(new_dir, 'w') as f:
        f.write("123")
    with open("new_file.txt") as f:
        print(f"{f.read() = }")
#new_directory()

def new_parse(): ## check solutions for finish answer
    with open("Homo_sapiens.GRCh38.107.abinitio.gtf") as f:
        for row in f:
          if not re.search('^\s*#', row): # ^ means first non-space character
              print(row.strip())
                cols = row.strip()
new_parse()


def main():
    # writing_to_text_files()
    # creating_and_modifying_paths()
    # parsing_text_files()
    return 0


if __name__ == '__main__':
    sys.exit(main())

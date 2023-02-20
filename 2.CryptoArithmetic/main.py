import os
import sys
import re


def main():
    try:
        with open(sys.argv[1], "r") as file:
            contents = file.read()
    except FileNotFoundError:
        print("Input file not found!")

    try:
        base = int(sys.argv[3])
    except IndexError:
        base = 10

    contents = re.sub(r'[+=\n]', ' ', contents)
    contents = contents.upper()
    letters = []
    for character in contents:
        if character not in letters and character != ' ':
            letters += character
    operators = contents.split()

    assert len(letters) <= base

    contents = "set(arithmetic).\nassign(domain_size, " + str(base) + ").\nassign(max_models, -1).\n\nlist(" \
                                                                      "distinct).\n\t["

    length = len(letters)
    for i in range(length):
        contents += letters[i]
        if i != length - 1:
            contents += ", "
    contents += "].\nend_of_list.\n\nformulas(assumptions).\n"

    for operator in operators:
        contents += "\t" + operator[0] + " != 0.\n"
    contents += "\t"

    length = len(operators)
    for i in range(length):
        j = len(operators[i])
        for character in operators[i]:
            factor = pow(base, j - 1)
            if factor == 1:
                contents += character
            else:
                contents += character + " * " + str(factor)
            j -= 1
            if (i == length - 2) and j == 0:
                contents += " = "
            elif not ((i == length - 1) and j == 0):
                contents += " + "
    contents += ".\nend_of_list.\n"

    try:
        with open(sys.argv[2], "w") as file:
            file.write(contents)
    except FileNotFoundError:
        print("Output file not found!")

    command = "mace4 -f " + sys.argv[2]
    os.system(command)


if __name__ == '__main__':
    main()

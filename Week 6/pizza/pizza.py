import csv
import sys
from tabulate import tabulate


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("too many command-line arguments")
    else:
        file = sys.argv[1]
        if file[-4:] != ".csv":
            sys.extit("Not a CSV file")
        else:
            print(tabulize(file))


def tabulize(file):
    try:
        with open(file) as file:
            reader = csv.reader(file)
            table = tabulate(reader, headers="firstrow", tablefmt="grid")
            return table
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
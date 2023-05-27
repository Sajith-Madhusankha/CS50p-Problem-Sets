import sys


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        file = sys.argv[1]
        if file[-3:] != ".py":
            sys.exit("Not a python file")
        else:
            print(count_lines(file))


def count_lines(file):
    try:
        count = 0
        with open(file) as file:
            for line in file:
                if not (line.lstrip().startswith("#") or line.strip() == ""):
                    count += 1
            return count
    except FileNotFoundError:
        sys.exit("file does not exist")


if __name__ == "__main__":
    main()
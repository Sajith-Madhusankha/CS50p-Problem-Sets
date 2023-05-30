import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    range = r"([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5])"
    if match := re.search(r"^" + range + "\." + range + "\." + range + "\." + range + "$", ip):
        return True
    else:
        return False


if __name__ == "__main__":
    main()

import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    octet = r"^(\d{1,3}\.){3}\d{1,3}$"

    if re.match(octet, ip):
        octets = ip.split(".")
        for set in octets:
            if (0<= int(set) <= 255):
                return True
            else:
                return False


if __name__ == "__main__":
    main()
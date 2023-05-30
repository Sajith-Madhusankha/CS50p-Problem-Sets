from datetime import date
import inflect
import sys
import operator

p = inflect.engine()


def main():
    try:
        birthday = input("Date of Birth: ")
        difference = operator.sub(date.today(), date.fromisoformat(birthday))
        print(convert(difference.days))
    except ValueError:
        sys.exit("Invalid date")


def convert(time):
    minutes = time * 24 * 60
    return f"{(p.number_to_words(minutes, andword='')).capitalize()} minutes"


if __name__ == "__main__":
    main()
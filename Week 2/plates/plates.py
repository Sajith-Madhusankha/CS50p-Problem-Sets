def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Get the length of the plate number
    length = len(s)

    # Check if plate number consist at least 2 numbers and at most 6 numbers
    if not 2 <= length <= 6:
        return False

    for letters in s:
        # Check if any character is not alphanumeric
        if not letters.isalnum():
            return False

        # Check if there are any numbers in the middle
        if letters.isalpha():
            index = s.find(letters)
            if index > 0:
                if s[index - 1].isdigit():
                    return False

    # Check if the first 2 characters are alphabetic characters
    if not s[0:2].isalpha():
        return False

    # Find the first zero and get the index of it
    zeroindex = s.find("0")

    # Check if 0 apperas first in numbers
    if zeroindex > 0:
        if s[zeroindex - 1].isalpha():
            return False


    # If all good, return true
    return True


main()

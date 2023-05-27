from PIL import Image, ImageOps
import sys
import os


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        format = [".jpg", ".jpeg", ".png"]
        inff = os.path.splitext(sys.argv[1])
        outff = os.path.splitext(sys.argv[2])
        if outff[1].lower() not in format:
            sys.exit("Invalid output")
        elif inff[1].lower() != outff[1].lower():
            sys.exit("Input and output have dinfferent extensions")
        else:
            editor(sys.argv[1], sys.argv[2])


def editor(input, output):
    try:
        shirt = Image.open("shirt.png")
        with Image.open(input) as input:
            cropped_input = ImageOps.fit(input, shirt.size)
            cropped_input.paste(shirt, mask = shirt)
            cropped_input.save(output)
    except FileNotFoundError:
        sys.exit("Input does not exist")


if __name__ == "__main__":
    main()

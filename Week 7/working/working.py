import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    time = "(0?[1-9]|1[0-2]):?([0-5][0-9])? (AM|PM)"
    if match := re.search(r"^" + time + " to " + time + "$", s):
        from_hour, from_minute = int(match.group(1)), (match.group(2))
        to_hour, to_minute = int(match.group(4)), (match.group(5))

        if match.group(3) == "PM":
            if from_hour == 12:
                from_hour = from_hour
            else:
                from_hour += 12

        elif match.group(6) == "PM":
            if to_hour == 12:
                to_hour = to_hour
            else:
                to_hour += 12

        if match.group(3) == "AM" and from_hour == 12:
            from_hour = 0
        elif match.group(6) == "AM" and to_hour == 12:
            to_hour = 0

        if from_minute == None:
            from_minute = 0
        else:
            from_minute = int(from_minute)
            if 1 > from_minute > 59:
                raise ValueError

        if to_minute == None:
            to_minute = 0
        else:
            to_minute = int(to_minute)
            if 1 > to_minute > 59:
                raise ValueError

        if 1 > to_hour > 12 or 1 > from_hour > 12:
            raise ValueError


        from_time = f"{from_hour:02}:{from_minute:02}"
        to_time = f"{to_hour:02}:{to_minute:02}"
        return f"{from_time} to {to_time}"
    else:
        raise ValueError



if __name__ == "__main__":
    main()

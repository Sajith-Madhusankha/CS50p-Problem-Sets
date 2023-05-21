months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input("Date: ")

    try:
        m, d, y = date.split("/")
        month = int(m)
        day = int(d)
        year = int(y)
        if (1 <= month <= 12) and (1 <= day <= 31):
            break

    except:
        try:
            mm, dd, yy = date.split(" ")
            for i in range(len(months)):
                if mm == months[i]:
                    month = i + 1

                day = dd.replace(",","")
                day = int(day)

            year = int(yy)

            if (1 <= month <= 12) and (1 <= day <= 31):
                break

        except:
            print()
            pass

print(f"{year}-{month:02}-{day:02}")
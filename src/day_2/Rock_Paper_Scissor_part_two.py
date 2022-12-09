def main():
    i = 0
    with open("input.txt", "r") as ifile:
        for line in ifile:
            a, b = line.split(" ")
            i += outcome(a.strip(),b.strip())
    print(i)


def outcome(a, b):
    x = 0
    if b == "X":
        x += 0
        if a == "A":
            x += 3
        elif a == "B":
            x += 1
        elif a == "C":
            x += 2
    elif b == "Y":
        x += 3
        if a == "A":
            x += 1
        elif a == "B":
            x += 2
        elif a == "C":
            x += 3
    elif b == "Z":
        x += 6
        if a == "A":
            x += 2
        elif a == "B":
            x += 3
        elif a == "C":
            x += 1

    return x


if __name__ == "__main__":
    main()

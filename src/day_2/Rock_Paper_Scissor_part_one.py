def main():
    i = 0
    with open("input.txt", "r") as ifile:
        for line in ifile:
            a, b = line.split(" ")
            i += outcome(a.strip(),b.strip())
    print(i)


def outcome(a, b):
    x = 0
    if a == "A":
        if b == "X":
            x += 1
            x += 3
        elif b == "Y":
            x += 2
            x += 6
        elif b == "Z":
            x += 3
            x += 0
    elif a == "B":
        if b == "X":
            x += 1
            x += 0
        elif b == "Y":
            x += 2
            x += 3
        elif b == "Z":
            x += 3
            x += 6
    elif a == "C":
        if b == "X":
            x += 1
            x += 6
        elif b == "Y":
            x += 2
            x += 0
        elif b == "Z":
            x += 3
            x += 3
    return x


if __name__ == "__main__":
    main()

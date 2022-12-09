def main():
    counter = 0
    counter2 = 0
    with open("input.txt", "r") as ifile:
        for line in ifile:
            a, b, c, d = line.replace('-', ',').split(sep=",")
            if (int(a) >= int(c) and int(b) <= int(d)) or (int(c) >= int(a) and int(d) <= int(b)):
                counter += 1
            if (int(a) >= int(c) and int(a) <= int(d)) or (int(c) >= int(a) and int(c) <= int(b)):
                counter2 += 1

        print(counter2)

if __name__ == "__main__":
    main()

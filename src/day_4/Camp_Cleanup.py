def main():
    counter = 0
    counter2 = 0
    with open("input.txt", "r") as ifile:
        for line in ifile:
            a, b, c, d = line.replace('-', ',').split(sep=",")
            list_a = []
            list_b = []
            for number in range(int(a), int(b)+1):
                list_a.append(int(number))
            for number in range(int(c), int(d)+1):
                list_b.append(int(number))

            rest_for_a = [x for x in list_a + list_b if x not in list_a]
            rest_for_b = [x for x in list_a + list_b if x not in list_b]

            rest_for_assignment_2 = [x for x in list_a + list_b if x in list_a and x in list_b]
            if rest_for_a == [] or rest_for_b == []:
                counter += 1
            if rest_for_assignment_2:
                counter2 += 1
    print(counter2)


if __name__ == "__main__":
    main()

def main(list):
    my_list = []
    with open("input.txt", "r") as ifile:
        for line in ifile:
            found = False
            a = line[0:len(line)//2].strip()
            b = line[len(line)//2:-1].strip()
            for letter_in_a in a:
                if found:
                    break
                for letter_in_b in b:
                    if letter_in_a == letter_in_b:
                        my_list.append(letter_in_b)
                        found = True
                        break
    sum_of_letters = 0

    for letter in my_list:
        sum_of_letters += list[letter]
    print(sum_of_letters)


def make_list():
    row_of_letters= {}
    j = 1
    for i in range(97,123):
        row_of_letters[chr(i)] = j
        j+=1
    for i in range(65,91):
        row_of_letters[chr(i)] = j
        j+=1
    return row_of_letters


if __name__ == "__main__":
    list = make_list()
    main(list)

def main():
    my_list = []
    with open("input.txt", "r") as file:
        lines_list = file.readlines()
    for line in range(0,len(lines_list)-2, 3):
        for char in lines_list[line]:
            if char.strip() in lines_list[line+1].strip() and char in lines_list[line+2].strip():
                my_list.append(char)
                break
    sum_of_letters = 0
    for letter in my_list:
        sum_of_letters += letter_to_number(letter)
    print(sum_of_letters)


def letter_to_number(letter):
    row_of_letters = {}
    j = 1
    for i in range(97, 123):
        row_of_letters[chr(i)] = j
        j += 1
    for i in range(65, 91):
        row_of_letters[chr(i)] = j
        j += 1
    return row_of_letters[letter]


if __name__ == "__main__":
    main()

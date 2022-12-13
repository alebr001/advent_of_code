def main():
    with open("input.txt", "r") as file:
        fileline = file.readlines()

    # # PART A
    for char in range(0,len(fileline[0])-1,1):
        if fileline[0][char] != fileline[0][char + 1] \
                and fileline[0][char] != fileline[0][char + 2] \
                and fileline[0][char] != fileline[0][char + 3] \
                and fileline[0][char + 1] != fileline[0][char + 2] \
                and fileline[0][char + 1] != fileline[0][char + 3] \
                and fileline[0][char + 2] != fileline[0][char + 3]:
            print(char + 4)
            break

    # PART B (kan ook voor part a gebruikt worden)
    list_different_chars = []
    length_of_marker = 14
    for char in range(len(fileline[0])-1):
        # put every new char in a list if it is not already in that list
        if fileline[0][char] not in list_different_chars:
            list_different_chars.append(fileline[0][char])
            if len(list_different_chars) == length_of_marker:
                print("length", len(list_different_chars))
                # +1 to convert from index to i-th number
                print(char+1)
                break
        # if it is already in the list, find the occurrence and delete everything preceding including the letter itself
        else:
            index = list_different_chars.index(fileline[0][char])
            list_different_chars = list_different_chars[index+1:]
            list_different_chars.append(fileline[0][char])


if __name__ == "__main__":
    main()
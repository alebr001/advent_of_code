def main():
    with open("input.txt", "r") as file:
        lines_list = file.readlines()

    # # PART A
    for char in range(0,len(lines_list[0])-1,1):
        if lines_list[0][char] != lines_list[0][char + 1] \
                and lines_list[0][char] != lines_list[0][char + 2] \
                and lines_list[0][char] != lines_list[0][char + 3] \
                and lines_list[0][char + 1] != lines_list[0][char + 2] \
                and lines_list[0][char + 1] != lines_list[0][char + 3] \
                and lines_list[0][char + 2] != lines_list[0][char + 3]:
            print(char + 4)
            break

    # PART B
    list_of_chars = []
    length_of_marker = 14
    for char in range(len(lines_list[0])-1):
        if lines_list[0][char] not in list_of_chars:
            list_of_chars.append(lines_list[0][char])
            if len(list_of_chars) == length_of_marker:
                print(char)
                break
        else:
            list_of_chars = [lines_list[0][char]]


if __name__ == "__main__":
    main()
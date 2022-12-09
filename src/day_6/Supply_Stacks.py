def main():
    with open("input.txt", "r") as file:
        lines_list = file.readlines()

    for char in range(0,len(lines_list[0])-1,1):
        if lines_list[0][char] != lines_list[0][char + 1] \
                and lines_list[0][char] != lines_list[0][char + 2] \
                and lines_list[0][char] != lines_list[0][char + 3] \
                and lines_list[0][char + 1] != lines_list[0][char + 2] \
                and lines_list[0][char + 1] != lines_list[0][char + 3] \
                and lines_list[0][char + 2] != lines_list[0][char + 3]:
            print(char + 3)
            break

if __name__ == "__main__":
    main()
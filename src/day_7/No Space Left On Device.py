from src.day_7.Folder import Folder
# create the root for no specific reason
root_folder = Folder("/", [], [])


def main():
    # set the current dir to the root
    cur_dir = root_folder

    # read the file and set a var to calculate all folders under 100.000
    file = read_file("input.txt")
    calculate_max_100000 = 0

    # for every row in the input file check if it is a command or a file/folder
    for row in file:
        if "$" in row:
            # if command to check if there is '..'. To calculate variable
            # 100.000 you have to start at the lowest folder and add the file
            # sizes of the folder under current folder as well
            if "$ cd" in row:
                dir_name = row.split(" ")[2]
                if dir_name == "..":
                    # get file size of the current directory (before going up one)
                    sub_dir_file_size = cur_dir.get_total_file_size()
                    # if it is lower then 100.000 then add it to the var
                    if cur_dir.get_total_file_size() <= 100000:
                        calculate_max_100000 += cur_dir.get_total_file_size()
                    # set the cur_dir to the parent
                    cur_dir = cur_dir.get_parent()
                    # add the file size of the subdirectory to the current directory
                    cur_dir.add_size_group_total(sub_dir_file_size)
                cur_dir = cur_dir.get_folder(dir_name)
        # if not a command then it is a file/folder, with a folder we add a new folder
        # and with a file we add the file size of the file to the total file size of
        # the group
        else:
            if "dir" in row:
                dir_name = row.split(" ")[1]
                cur_dir.add_folder(Folder(dir_name, [], [], cur_dir))
            elif " " in row:
                size, file = row.split(" ")
                size = int(size)
                # cur_dir.add_file(file)
                cur_dir.add_size_group_total(size)

    print("cur own name", cur_dir.get_own_name())
    print(calculate_max_100000)


def read_file(filename):
    with open(filename) as file:
        return file.read().split('\n')


if __name__ == "__main__":
    main()

from src.day_7.Folder import Folder
# create the root folder
root_folder = Folder("/", [], [])
max_file_system_size = 70000000
update_size = 30000000


def main():
    # set the current dir to the root
    cur_dir = root_folder
    calculate_max_100000 = 0
    # read the file and set a var to calculate all folders under 100.000
    file = read_file("input.txt")

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


def main2():
    # set the current dir to the root
    cur_dir = root_folder
    # make list where every folder of directory is put in
    # because this makes it easy to loop over all folders
    list_of_all_folders = []
    file = read_file("input.txt")
    # for every row in the input file check if it is a command or a file/folder
    for row in file:
        # ls does nothing in my solution but if there is no dollar then it is the folder content
        if "$" in row:
            if "$ cd" in row:
                # get dir name to later go into
                dir_name = row.split(" ")[2]
                if dir_name == "..":
                    # set the cur_dir to the parent
                    cur_dir = cur_dir.get_parent()
                cur_dir = cur_dir.get_folder(dir_name)
        # if not a command then it is content, with a folder we add a new folder instance and
        # with a file we add the file size of the file to the total file size of the group
        else:
            if "dir" in row:
                dir_name = row.split(" ")[1]
                new_folder = Folder(dir_name, [], [], cur_dir)
                cur_dir.add_folder(new_folder)
                list_of_all_folders.append(new_folder)
            elif " " in row:
                size, file = row.split(" ")
                size = int(size)
                cur_dir.add_size_group_total(size)

    # make two variables for readability, one with root storage and the
    # other is the amount of storage needed for the update
    root_storage = root_folder.get_total_storage()
    storage_needed = max_file_system_size - update_size
    print("total storage: ", root_storage)
    print("root folder should decrease", root_storage - storage_needed, end='\n\n')

    folder_name = ""
    size_of_folder_to_delete = update_size

    for folder in list_of_all_folders:
        if root_storage - storage_needed <= folder.get_total_storage() <= size_of_folder_to_delete:
            size_of_folder_to_delete = folder.get_total_storage()
            folder_name = folder.get_own_name()

    print(folder_name, "is the smallest with this amount of data:", size_of_folder_to_delete)



def read_file(filename):
    with open(filename) as file:
        return file.read().split('\n')


if __name__ == "__main__":
    main2()

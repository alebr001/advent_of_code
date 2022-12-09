import numpy as np


def main():
    with open("input.txt", "r") as file:
        lines_list = file.readlines()

    # create a list with the commands
    commands = lines_list[10:]

    ##### ASSIGNEMNT A #####
    # create a list with the crates
    list_of_list_of_crates = get_list_of_crates(lines_list)

    # for every command, get the integers out and put them in vars
    for command in commands:
        command = command.replace("move ","").replace(" from ", ":").replace(" to ", ":").replace("\n","")
        mv, frm, t = command.split(":")
        mv, frm, t = int(mv), int(frm), int(t)

        # for every move append the crate to the list where it needs to go and then delete the original
        for i in range(mv):
            list_of_list_of_crates[t-1].append(list_of_list_of_crates[frm-1][-1])
            del(list_of_list_of_crates[frm-1][-1])

    # print out only the last record of each list
    for lst in list_of_list_of_crates:
        print(lst[-1], end="")

    print()
    ##### ASSIGNEMNT B #####
    list_of_list_of_crates = get_list_of_crates(lines_list)
    for command in commands:
        command = command.replace("move ","").replace(" from ", ":").replace(" to ", ":").replace("\n","")
        mv, frm, t = command.split(":")
        mv, frm, t = int(mv), int(frm), int(t)

        list_of_list_of_crates[t-1].extend((list_of_list_of_crates[frm-1][-mv:]))
        del(list_of_list_of_crates[frm-1][-mv:])

    # print out only the last record of each list
    for lst in list_of_list_of_crates:
        print(lst[-1], end="")


def get_list_of_crates(lines_list):
    crates = lines_list[0:9]
    list_of_crates = []

    # Put all rows in a list to transpose
    for row in crates:
        char_row = []
        for char in range(0, len(row), 4):
            char_row.append(row[char+1])
        list_of_crates.append(char_row)

    # transpose and empty the original list
    transposed = np.array(list_of_crates).T.tolist()
    list_of_crates = []

    # reverse the order of the lists in the list of crates and remove the spaces
    for lst in transposed:
        lst.reverse()
        list_of_crates.append(remove_spaces(lst))

    return list_of_crates


def remove_spaces(lst):
    res = [i for i in lst if i != ' ']
    return res


if __name__ == "__main__":
    main()

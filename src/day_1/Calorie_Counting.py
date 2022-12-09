def dat_fun():
    mylist = []
    i = 0
    with open("input.txt", "r") as ifile:
        for line in ifile:
            if not line.strip():
                mylist.append(i)
                i = 0
                continue
            i += int(line)
    mylist.sort(reverse=1)
    print(mylist[0]+mylist[1]+mylist[2])


dat_fun()

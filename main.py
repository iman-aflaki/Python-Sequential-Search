def sequential_search(my_list,num):
    pos = 0
    found = False
    while num != my_list[pos] and not found:
        if num == my_list[pos]:
            found = True
        else:
            pos += 1
    return pos
my_list = [23,453,567,8776,454,23,54,23,12]
print(sequential_search(my_list,454))

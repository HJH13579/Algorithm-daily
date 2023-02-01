lst = [6, 9, 12, 15, 18, 21, 24, 27]


def count(lst_1):
    num = 0

    for _ in lst_1:
        num += 1

    return num


def my_max(lst_2):
    max_num = lst_2[0]

    for x in range(1, count(lst_2)):
        if lst_2[0] < lst_2[x]:
            lst_2[0] = lst_2[x]
        else:
            lst_2[0] = lst_2[0]

    return max_num


print(my_max(lst))

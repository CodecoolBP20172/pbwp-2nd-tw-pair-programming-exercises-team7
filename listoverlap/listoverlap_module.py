from random import *

def listoverlap(list1, list2):
    overlap_set = set()
    for i in range(len(list1)):
        if list1[i] in list2:
            overlap_set.add(list1[i])
    return list(overlap_set)

def rand_list():
    tmp_list = []
    rand_range = randint(5, 15)
    for i in range(rand_range):
        tmp_list.append(randint(1, 20))
    return tmp_list

def main():
    list_1 = rand_list()
    list_2 = rand_list()
    print(list_1)
    print(list_2)

    list_3 = listoverlap(list_1, list_2)

    print (list_3)
    return


if __name__ == '__main__':
    main()

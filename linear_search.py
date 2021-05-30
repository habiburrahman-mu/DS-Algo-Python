def linear_search(number_list, number_to_find):
    for index, element in enumerate(number_list):
        if element == number_to_find:
            return index
    return -1


if __name__ == '__main__':
    li = [12, 15, 17, 19, 21, 24, 45, 67]
    number = 12
    ind = linear_search(li, number)
    print(ind)


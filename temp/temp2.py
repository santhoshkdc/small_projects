empty_list = []

for i in range(5):
    empty_list.append(list('*' * 9))
for index_a, i in enumerate(empty_list):
    for index_b, j in enumerate(i):
        if index_a % 2 == 1:
            if index_b % 2 == 0:
                i[index_b] = ' '
        elif index_a % 2 == 0:
            if index_b % 2 == 1:
                i[index_b] = ' '

for i in empty_list:
        print("".join(i), end="\n")
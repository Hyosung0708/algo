my_list = [1, 6, 3, 9, 0, 7, 2, 2]


# 버블정렬
for i in range(len(my_list)-1, 0, -1):
    for j in range(i):
        left = my_list[j]
        right = my_list[j+1]

        # print(left, right)

        if left > right:
            my_list[j], my_list[j+1] = my_list[j+1], my_list[j]

            # temp = my_list[j]
            # my_list[j] = my_list[j+1]
            # my_list[j+1] = temp
print(my_list)


# 카운팅정렬
counter = [0 for i in range(10)]

for i in my_list:
    counter[i] += 1

result = []

for value, count in enumerate(counter):
    for i in range(count):
        result.append(value)

print(result)


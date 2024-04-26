first_list = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
for i in range(first_list.count(0)):
    first_list.remove(0)
    first_list.append(0)
print(first_list)
first_list = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
i = 0
while i < len(first_list):
    if first_list[i] == 0:
        first_list.remove(0)
        first_list.append(0)
    i += 1
print(first_list)
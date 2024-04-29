# Зрізи
lst = [12, 6, 3, 41, 9, 2, 3, 11, 13]
# lst = [1]
# lst = []
# lst = [1, 2, 3, 4]
if len(lst) % 2 == 0:
    n = len(lst) // 2
else:
    n = len(lst) // 2 + 1
new_list = [lst[:n], lst[n:]]
print("Новий список: ", new_list)

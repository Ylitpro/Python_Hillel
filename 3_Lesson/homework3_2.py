lst = [23, 45, 6, 11]
if len(lst) != 0:
    lst.insert(0, lst.pop()) # вставка елементу на позицію 2, це індекс 1
    print(lst)
else:
    print(lst)
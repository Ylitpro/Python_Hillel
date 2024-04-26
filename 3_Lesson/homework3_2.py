lst = [12, 7, 3, 9, 11]
if len(lst) != 0:
    lst.insert(0, lst.pop())
    print(lst)
else:
    print(lst)
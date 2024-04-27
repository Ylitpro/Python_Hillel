# first_list = [0, 1, 7, 2, 4, 8]
# first_list = [6]
# first_list = []
first_list = [1, 3, 5]
Result = 0
if len(first_list) != 0:
    for i in range(len(first_list)):
        if i % 2 == 0:
            Result += first_list[i]
    Result = Result * first_list[-1]
print("Сума елементів з парними індексами =", Result)

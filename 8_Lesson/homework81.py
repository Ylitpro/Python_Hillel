def add_one(some_list: list) -> list:
    result = ''
    for i in range(len(some_list)):
        result += str(some_list[i])
    new_num = str(int(result) + 1)
    return [int(x) for x in str(new_num)]


assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")

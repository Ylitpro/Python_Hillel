def common_elements() -> set:
    first_list = set(range(0, 101, 3))
    second_list = set(range(0, 101, 5))
    return first_list.intersection(second_list)


assert common_elements() == {0, 75, 45, 15, 90, 60, 30}, 'Test 1'
print('OK')

def second_index(text: str, some_str: str):
    ind = text.find(some_str)
    if ind >= 0:
        new_ind = text.find(some_str, ind + 1)
        if new_ind > 0:
            return new_ind
        return None


assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')

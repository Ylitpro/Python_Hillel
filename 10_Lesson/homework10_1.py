def odd_num(x: int) -> int:
    return 2 * x + 1


def my_gen(begin, end, func):
    """
     Sequence of odd numbers
     begin: The first number of sequence
     end: The number of elements in the sequence
     func: The function that generates odd numbers
    """
    count = 0
    while count < end:
        yield begin
        begin = func(begin)
        count += 1


from inspect import isgenerator

gen = my_gen(5, 4, odd_num)
assert isgenerator(gen) == True, 'Test1'
assert list(gen) == [5, 11, 23, 47], 'Test2'
print('OK')

def is_even(digit: int) -> bool:
    """
     Checking whether the number is even or odd
     digit: The number for checking
     """
    return digit % 2 == 0


assert is_even(2) == True, 'Test1'
assert is_even(5) == False, 'Test2'
assert is_even(0) == True, 'Test3'
print('OK')

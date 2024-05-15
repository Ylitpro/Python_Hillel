def add(x, y) -> int:
    def test():
        print("test")

    return x + y


sum_of_two_elements = add

print(add(1, 1))
print(sum_of_two_elements(1, 1))


def apply_oper(data: list[int], operation) -> list:
    res = []
    for element in data:
        res.append(operation(element))
    return res


def square(number: int) -> int:
    return number ** 2


def double(number: int) -> int:
    return number * 2


numbers = [1, 2, 3, 4, 5]

squared_numbers = apply_oper(numbers, square)
doubled_numbers = apply_oper(numbers, double)

print(squared_numbers)
print(doubled_numbers)


# --------------------------------

# рекурсії
# 6!=1*2*3*4*5*6
def factorial(number: int) -> int:
    if number == 0 or number == 1:
        return 1
    else:
        return number * factorial(number - 1)


print(factorial(6))


# ---------------------
# Анонімні функції - lamda функції

def double(x):
    return x*2


double_two = lambda x: x**2
print(double_two(5))

check_even = lambda x: True if x% 2 == 0 else False
print(check_even(2))
print(check_even(3))

# --------------------

numbers = [1, 2, 3, 4, 5]

res = []
for elem in numbers:
    res.append(elem**2)

# або так

square_numbers = map(lambda x: x**2, numbers)
result = list(square_numbers)
print(result)

#----------------
numbers = [1, 2, 3, 4, 5, 6, 7]

filtered_numbers = filter(lambda x: x % 2 == 0, numbers)
result = list(filtered_numbers)
print(result)

# ------------------

ages = [21, 22, 23]
names = ["Andriy", "Alex", "Katya"]

zipped = zip(names, ages)
result = list(zipped)
print(result)

#------------------------------

numbers = [1, 2, 3, 4, 5, 6, 7]

filtered_numbers = map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers))
result = list(filtered_numbers)
print(result)

# ---------------------
# Генератори

def my_generator():
    yield 1
    yield 2
    yield 3

print(next(my_generator()))

# Фібоначчі

def fibonachi_generator(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

fibonachi = fibonachi_generator(250)

for value in fibonachi:
    print(value)



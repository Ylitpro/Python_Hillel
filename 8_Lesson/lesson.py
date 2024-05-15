# Глобальні та локальні змінні
global_var = "World"

# def example():
#     print(global_var)
#     print("World")
#
# example()

def example():
    local_var = "Hello"

    return local_var + global_var

print(example())
# LEGB
# L- Local
# E - Enclosing (працює для вкладених функцій)
# G -Global
# B - Built in

def example():
    local_var = "Local"
    def test():
        inner = "Inner"
        print(inner)
        print(local_var)
        print(global_var)
        print()

    test()
    return local_var + global_var

print(example())

# Передача аргументів до функції
def summ_of_ele(x:int, y: int) -> int:
    return x + y

print(summ_of summ_of_ele(y=2, x=1))
print(summ_of_ele(1,2 ))

# Оголошення змінних
# args  - кількість змінних
def summ_of_ele(*args) -> int:
for arg in args:
    print(arg)

summ_of_ele(1,2,3,4,5,"7","9",0)

def summ_of_ele(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(key, value)


summ_of_ele("7","8","9",0, num_1=1,num_2=2, num_3=3)


# Приклад 2
def example(positional, named, *args, **kwargs):
    print(f"Positional: {positional}")
    print(f"Named: {named}")
    print(f"Additional position: {args}")
    print(f"Additional named: {kwargs}")

example(positional:"7", named=8, mas=1)

# Анотація до коду
def calculate_square(radius: int) -> float:
    """
    calculate the square of cirle
    :param radius: The radius of the cirle
    :return: The square of the cirle
    """
    square = 3.14 * (radius ** 2)
    return square

print(help(calculate_square()))


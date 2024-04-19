user_input = input("Введіть 4-значне ціле число: ")
x = int(user_input)
x1 = x // 1000
x2 = (x % 1000) // 100
x3 = ((x % 1000) % 100) // 10
x4 = x % 10
print(x1)
print(x2)
print(x3)
print(x4)

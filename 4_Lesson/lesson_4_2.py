# Цикли
n=1
while  n < 10:
    print(n)
    if n == 5:
        continue
    n += 1

n=1
while  n < 10:
    n += 1
    if n == 5:
        continue
    print(n)

n=1
while  n < 10:
    n += 1
    if n == 5:
        break
    print(n)

print("end")

n=1
while  n < 10:
    n += 1
    if n == 5:
        continue
    if  n == 9:
        break
     print(n)
print("end")

n=1
while  n < 10:
    n += 1
    j = 1
    print(n)
    while j < 10:
        j += 1
        print(j)
print("end")

i = 0
first_list = [4, 3, 5, 2, 9, 7]
while i < len(first_list)
    print(first_list[i])
    i += 1
print("_______")

for elem in first_list:
    print(elem)

x = range(5)
for elem in x:
    print("1")

x = range(5) # генератор числової послідовності
x = 0,1,2,3,4
x = range(5, 10) # проміжок від 5 до 10
x = range(5,10,2) # крок 2 - виведення чисел 7, 9
for elem in x:
    print("1")
    break
else:
    print("end")


print(enumerate(first_list)) # enumerate зберігає індекс і значення списку
for index, elem in enumerate(first_list)
    print(index,"->", elem)

# Модуль random

import random
for _ in range(100):
    print(random.random)
    print(random.randint(1,100))
    print(random.choice(first_list)) # вибір елементу зі списку
    random.shuffle(first_list) # розміщує у довільному порядку
    print(first_list)










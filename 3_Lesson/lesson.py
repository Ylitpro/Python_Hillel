x = int(input("Enter number"))
y = int(input("Enter number"))
if y == 0 and x == 4:
    print("Null forbiden")
    if x == 0:
        print("0")
elif y ==1:
    print("")
else:
    p = x / y
    print (p)
if not y != 0 or x ==5:

x = 10
y = 20
if x > y:
    z = x
else:
    z = y

z = x if x > y else y

None
list = []
c = list.append(1)
print(list)
print (c)

lst = [1,4,5, True, "3", [6,7]]
print(lst)
lst_1 = list()
lst[-1].append(8) # додає елемент у кінець списку
lst.insert(1,9) # вставка елементу на позицію 2, це індекс 1
lst[1] = 2 # змінити значення другого елементу списку

lst.remove(1) #видаляє значення 1 зі списку, яке зустрічається першим
lst.pop(0) # видаляє значення елементу з індексом 0 і виводить значення видаленого елементу
del lst[0] # видаляє елемент

1 in lst # перевірити входить елемент у список чи ні
print(1 in lst)

print(len([1,2,3])) # len визначає довжину спсику

# Конкатенація, обєднання списків
x = [1,2]
y = [3,4]
print(x + y)
x.extend(y) # це також обєднання

# Продублювати елементи у списку n -разів
y = [3,4]*3 # повторення 3 рази
print(y)

# Зрізи
x = [1,2,3,4,5]
y = x[0:3] # вивести список з 0 елементу до 2
y = x[2:] # вивести список з 2 елементу до останнього елементу
print(y)
y = x[10:101:5] # вивести елементи з кроком 5
y = x[:] # скопіювати список з тим, щоб створити новий список з новою адресою





print(lst[0]) # номер індексу першого елементу
print(lst[-1]) # номер останнього елементу
print(lst[-2]) # номер передостаннього елементу
print(lst[-1],[0]) # виведе 6





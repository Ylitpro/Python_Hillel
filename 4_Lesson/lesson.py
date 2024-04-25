first_list = [2, 4, 5, 6, 7]
first_list[1:3] = [6, 7, 8] # заміна елементів в списку
print(first_list)

first_list = [4, 3, 5, 2, 9, 7]
print(first_list.count(6)) # рахує кількість символу 6
print(first_list.index(6)) # видає індекс
print(first_list.sort()) # сортує список, якщо список з одного типу
print(first_list.sort(reverse=True))

# Копіювання списків
first_list = [4, 3, 5, 2, [9, 7]]
second_list = first_list.copy()  # адреси списків при такому методі змінюються
print(id(second_list) == id(first_list))
print(id(second_list[-1]) == id(first_list[-1]))
first_list[-1].append(8)
print(first_list)
print(second_list)

# Бібліотека copy
import copy
first_list = [4, 3, 5, 2, [9, 7]]
second_list = copy.deepcopy(first_list)
print(id(second_list[-1]) == id(first_list[-1]))
first_list[-1].append(8)
print(first_list)
print(second_list)

# clear  метод очищення списку
import copy
first_list = [4, 3, 5, 2, [9, 7]]
second_list = copy.deepcopy(first_list)
print(id(second_list[-1]) == id(first_list[-1]))
first_list[-1].append(8)
print(first_list)
second_list.clear()
print(second_list)

#  Мінімум і максимум
first_list = [4, 3, 5, 2, 9, 7]
print(min(first_list))
print(max(first_list))
print(all(first_list))
print(any(first_list))
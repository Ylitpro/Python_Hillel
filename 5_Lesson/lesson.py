# рядки
string = "text2"
print(string)
string = 'Text "like"'
print(string)

#Екранування символів
string = 'Text \'like\''
print(string)

string = "123"
int(string)

number = 12345
str_number = str(number)
print(str_number)
print(type(str_number))

# Робота з рядками як і зі списками
string = "I like Python"
print(string[3])
print(string[:4]) #зрізи

# Конкатенація рядків
string = "I like Python!"
new_string = "I like Java too"
print(string + new_string)
print(string * 5)

# Змінити елемент рядка
# як у списках
array = [1,2,3]
array[0] = 10
print(array)

for character in string:
    print(character)

# Пошук підрядка у рядку
if "Python" in string:
    print ("Yes")
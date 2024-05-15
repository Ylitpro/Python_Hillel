# Методи роботи з рядками
string = "I like Python!"

upper_string = string.upper() # перевести всі літери у заголовні
print(upper_string)
lower_string = upper_string.lower()
print(lower_string)

#
string = "i like python"
title_string = string.title()
print(title_string)

swap_string = title_string.swapcase()
print(swap_string)

# email = input("Please your email")
#print(email.strip()) # прибирає пробіли у слова і справа, і зліва
# print(email.lstrip()) # прибирає пробіли у слові зліва

#string = "I like PHP! PHP!"
#new_string = string.replace("PHP", "Python", 1)
#print(new_string)

# Розбити рядок на елементи списку
string = "I like dogs and cats"
array = string.split()
print(array)

string = "I like dogs, cats"
array = string.split(",")
print(array)

string = "I like dogs, cats"
array = string.split("o")
print(array)

array = ["I", "like", "Python", "Python"]
joined_string = ",  ".join(array)
print(joined_string)

print(joined_string.find("th", ))
print(joined_string.count("th", )) # скільки разів зустрічається

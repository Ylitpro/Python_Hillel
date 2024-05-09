import string

s = string.ascii_letters
string = input("Enter letters:")
array = string.split("-")
print(s[s.find(array[0]):(s.find(array[1]) + 1)])

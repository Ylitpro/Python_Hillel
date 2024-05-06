import string
my_string = input("Введіть текст для хештегу:").title()
result = '#'
for i in my_string:
    if len(result) > 140:
        break
    if i in string.punctuation or i == ' ':
        continue
    else:
        result += i
print(result)


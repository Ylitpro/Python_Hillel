my_string = input("Enter number:")
while True:
    x = 1
    for char in my_string:
        x *= int(char)
    if x <= 9:
        break
    my_string = str(x)
print(x)



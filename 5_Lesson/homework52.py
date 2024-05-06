while True:
    a = int(input("Введіть перше число:"))
    b = int(input("Введіть друге число:"))
    c = input("Введіть дії, яку потрібно виконати (+-*/):")
    if b != 0 and c == "/":
        rez = a / b
        print("Результат обчислення:", rez)
    elif c == "*":
        rez = a * b
        print("Результат обчислення:", rez)
    elif c == "-":
        rez = a - b
        print("Результат обчислення:", rez)
    elif c == "+":
        rez = a + b
        print("Результат обчислення:", rez)
    else:
        print("Помилка, введено некоректні дані.")
    result = input("Якщо бажаєте продожити обчислення, то введіть 'y':")
    if result.lower() == "y":
        continue
    else:
        break

# байтові рядки
s = b"hello"
print(s)
s2 = "Hello, world!"
b = s2.encode("utf-8") # кодування символів
print(type(b))
print(b)
s = b.decode("utf -8")
print(type(s))
print(s)

# Кортеж  -це незмінний тип
def test(x):
    x += 1
    y = 2
    return x, y

numbers = test(1)

# стоврити кортеж
t = (1,)
i = (2)
print(type(t))
print(type(i))

t = tuple("help")
print(t)

t = (1, 2, 3, [1, 2, 3] )
print(len(t))
print(t[0]) # повертає індекс

a = 10
b = 20
a, b = b, a # змінити значення a, b
print(a)
print(b)

# Перевірити входження елементу
a = (1, "hello", 3)
if "hello" in a:
    print("True")

# Словники - змінний тип, невпорядкований тип; ключами можуть бути тільки незмінні типи даних
a = {"name": "Tanya",
     "age": 34,
     "fruits": ["apple", "banana"]
     }
print(a["name"])

# Створення
b = dict(name="Tanya", age=34)
print(len(a))

print("name" in a) # перевірка входження ключа у словник
print("sort" in a)

# Hash
print(hash("Hello"))
a = {"name": "Tanya",
     "fruits": {
         "sort": "red apple"
     }}
print(a["name"].upper())
print(a["fruits"]["sort"].upper())
a["fruits"]["sort"] = "Golden"
print(a)


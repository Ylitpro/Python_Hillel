import collections
d = collections.OrderedDict({  # зберегти порядок ключів і значень в словнику
    "name": "Tasya",
    "age": "35",
})
d.popitem(last=False) # видалити останній елемент?
print(d)

d = collections.defaultdict(list)
print(d["name"])

n = {}
n["key"] = 123
print(n)

Point = collections.namedtuple("Point", "x y")
p = Point(3, 4)
print(type(p))
print(p.x)
print(p.y)

print(p[0])

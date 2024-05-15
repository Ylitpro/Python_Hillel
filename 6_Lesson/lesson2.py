import copy
a = {"name": "Tanya",
     "fruits": {
         "sort": "red apple"
     }}
b = a.copy() # копія
b["fruits"]["sort"] = "Golden"
print(a)

b1 = copy.deepcopy(a)
b["fruits"]["sort"] = "Golden"
print(a)

#
m = dict.fromkeys([1, "a", 2, "b"], "test")
print(m)
#m["a"].append  ???

d = {}
for elem in [1, "a", 2, "b"]:
    d[elem] = []
print(d)
d["age"] =27
print(d.get("age", 27)) # додати ключ
print(d)
print(d.items()) # виведення пар ключ-значення

for key, value in d.items():
    print(key)
    print(value)
name = d.get("age")
print(name)

print(d.keys())
# це теж саме, що
for elem in d.items():
    print(elem)

print(d.pop("l", "test"))
print(d)




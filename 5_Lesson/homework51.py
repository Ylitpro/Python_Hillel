import keyword
value = input("Enter your text:")
if value in keyword.kwlist or not value.lower() == value or not value.isidentifier():
    print("False")
else:
    print("True")

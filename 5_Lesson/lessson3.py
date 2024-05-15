#value = input("Please enter number of apple:")
#if not value.isdigit(): # рядок складається з цифр
#    print("Error")
#else:
 #   print(f"You got {value} apples")

#number = input("Please enter number")
#x = int(number)
#12
# print(x*5)

string = "I like Python"
print(string.startswith("I"))
print(string.startswith("P"))
print(string.endswith("n"))

string = "1,2,3,1,2,3,1,2,3"
ind = string.find("1")
print(ind)
new_ind = string.find("1", ind+1)
print(new_ind)
third_ind = string.find("1", new_ind+1, new_ind+3)
print(third_ind)

# Форматування рядок
name = "Tanya"
age = 24
height = 1.81

string = "%s is %d years old and %f meters tall" % (name, age, height)
print(string)




character_name = "John"
character_age = "50.5678"
is_male = True
print("there once was a man named " + character_name + ",")
print("he was " + character_age + " years old")
print("he really liked the name " + character_name +",")
print("but he didnt like being " + character_age + ".")

print(character_name.isupper())
print(character_name.upper())
print(character_name.lower())

print(len(character_name))
print(character_name[2])
print(character_name.index("J"))
print(character_name.replace("John","Tom"))

print(2.09 * 4.6)
my_num = 5
print(str(my_num) + " my fav num")

name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello " + name + "!")
print("You are " + age + " years old")

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = int(num1) + int(num2)
print(result)

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = float(num1) + float(num2)
print(result)
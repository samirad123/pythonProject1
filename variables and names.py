cars = 100
space = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space
average_passengers_per_car = passengers / cars_driven

print(f"There are {cars} cars available.")
print(f"There are only {drivers} drivers available.")
print(f"There will be {cars_not_driven} empty cars today.")
print(f"We can transport {carpool_capacity} people today.")
print(f"We have {passengers} to carpool today.")
print(f"We need to put about {average_passengers_per_car} in each car. ")

#another way
types_of_people = 10
x = f"There are {types_of_people} types of people."
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said : {x}")
print(f"I also said :{y}")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with right side."

print(w + e)

#another way
print("Mary had a little lamb.")
print("Its fleece was white as {}.".format('snow'))
print("And everywhere that Mray went.")
print("." * 10)

end1 = "C"
end2 = "H"
end3 ="E"
end4 ="E"
end5 ="S"
end6 ="E"
end7 ="B"
end8 ="U"
end9 ="R"
end10 ="G"
end11 ="E"
end12 ="R"

print(end1 + end2 + end3 + end4 + end5 + end6,end = " ")
print(end7 + end8 + end9 + end10 + end11 + end12)

#another way
formatter = "{} {} {} {}"

print(formatter.format(1,2,3,4))
print(formatter.format("one","two","three","four"))
print(formatter.format(formatter,formatter,formatter,formatter))
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe your own poem",
    "Or about a song you fear",
))

#another way
days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print("Here are the days:",days)
print("Here are the months:",months)

print("""
There's something going on here
with 3 double quotes.
""")

#another way
tabby_cat = "\tI'm tabbed in."
persian_cat = "\tI'm split\non a line."
backlash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* fishies
\t* catnip\n\t* grass
"""

print(tabby_cat)
print(persian_cat)
print(backlash_cat)
print(fat_cat)

#another way
print("How old are you? :",end = '')
age = input()
print("How tall are you? :", end = '')
height = input()
print("How much do you weigh? :", end = '')
weight = input()

print(f"so you are {age} years old ,{height} tall and weigh {weight}")


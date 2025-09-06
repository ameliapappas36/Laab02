#!/usr/bin/env python3

#name variables
name = "Amelia"
age = 21
height = 5.7
favorite_color = "Teal"

#print variables
print(name)
print(age)
print(height)
print(favorite_color)

print(name, age, height, favorite_color)

print(f"Hello I am {name} and I am {age} years old. I am {height} and love {favorite_color}.")

print(f"""

Name: {name}

Age: {age}

Height: {height}

Favorite Color: {favorite_color}

""")

import math

#radius of a circle
r = 5
circle_area = (math.pi * r**2)
print(round(circle_area, 1))

print(math.sqrt(age))

print(math.sin(height))
print(math.cos(height))

#math from lab2
a = age + 5
b = height - 4
c = age + height
d = height / 2
e = age % (age + 1)
f = age**2
print(a, b, c, d, e, f)

temp_farenheit = float(input(f"{name} enter a temperature in Farenheit: "))
celsius = (temp_farenheit - 32) * (5/9)
print(f"Temp Farenheit {temp_farenheit}°F in Celsius is {celsius}°C")

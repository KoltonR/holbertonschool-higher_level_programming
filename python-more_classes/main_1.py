#!/usr/bin/python3
Rectangle = __import__('6-rectangle').Rectangle

print(Rectangle.number_of_instances)
r_1 = Rectangle(12, 4)
print(Rectangle.number_of_instances)
del r_1

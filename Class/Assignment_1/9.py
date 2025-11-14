# 9. Write a python program to find the area and volume of sphere.

import math

r = float(input("Enter radius of the sphere: "))

area = 4 * math.pi * r * r
volume = (4/3) * math.pi * r * r * r

print("Surface Area =", area)
print("Volume =", volume)
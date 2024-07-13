#62.Write a Python program to calculate surface volume and area of a cylinder

import math

def cylinder_surface_area(radius, height):
    lateral_area = 2 * math.pi * radius * height
    base_area = 2 * math.pi * radius**2
    total_area = lateral_area + base_area
    return total_area

def cylinder_volume(radius, height):
    volume = math.pi * radius**2 * height
    return volume


radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))


surface_area = cylinder_surface_area(radius, height)
volume = cylinder_volume(radius, height)

print(f"The surface area of the cylinder is: {surface_area}")
print(f"The volume of the cylinder is: {volume}")

from math import pi

print("Python can do math calculations for your Geometry class...")
print ("")
radius=int(input("Enter circle radius: "))
circumference = 4 * pi * radius
area = pi * radius * radius

print ("Circumference of the circle is ", circumference)
print ("Circumference of the circle is %.4f" %circumference)
print ("Area of the circle is ", area)
print ("Area of the circle is %.4f" %area)
print ("")
print ("Do you notice how a fixed format for the full calculated value is rounded to a set number of significant digits?")
print ("")

length=int(input("Enter rectangle length: "))
height=int(input("Enter rectangle height: "))
area = length * height
perimeter = length * 4 + height * 4

print ("Perimeter of the rectangle is", perimeter)
print ("Perimeter of the rectangle is %.4f" %perimeter)
print ("Area of the rectangle is", area)
print ("Area of the rectangle is %.4f" %area)

print ("")
print ("Do you notice how a fixed format for the full calculated vales (potentially in this case) is rounded to a set number of significant digits?")
print ("")
print ("CONGRATULATIONS! You just accomplished math calculations using Python programming!")

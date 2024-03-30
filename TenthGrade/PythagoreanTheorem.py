import math
import os
print("Pythagorean Theorem")
print("")
print("Please input the angles of the triangle.")
angleA=int(input("Enter measure of angle A: "))
angleB=int(input("Enter measure of angle B: "))
angleC=int(input("Enter measure of angle C: "))
angleD = angleA + angleB + angleC
print("")

if angleA == 90:
    print("")

elif angleB == 90:
    print("")
    
elif angleC == 90:
    print("")

else:
    print("THESE ANGLES ARE NOT COMPATABLE WITH THE PYTHAGOREAN THEOREM") 
    os._exit(0)

if angleD < 180 or angleD > 180:
    print("THESE ANGLES ARE NOT COMPATABLE WITH THE PYTHAGOREAN THEOREM") 
    os._exit(0)

else:  
    print("")
print("")
print("Please input 1 and 2 in the sides you have and input 3 for the side you don't have.")
print("")
print("This is an example. I know what both side A and side B values are so I put number 1 and number 2. But I did not know the value of side C so I put 3.")
print("")     
print("Side A = 1")
print("Side B = 2")
print("Side C = 3")
print("")
SideA=int(input("Side A: "))
SideB=int(input("Side B: "))
SideC=int(input("Side C: "))
SideD = SideA + SideB + SideC
print("")

if SideD > 6 or SideD < 6:
    os._exit(0)

if SideA == 3 or SideA == 2 or SideA == 1:
    print("")

elif SideB == 3 or SideB == 2 or SideB == 1:
    print("")

elif SideC == 3 or SideC == 2 or SideC == 1:
    print("")

else:
    os._exit(0)
    
if SideA == 2 and SideB == 2 and SideC == 2:
    os._exit(0)

else:
    print("")
    
if SideC > 2:
    n=int(input("Enter the length of side A: "))
    n2 = n**2

    n3=int(input("Enter the length of side B: "))
    n4 = n3**2

    n5 = n2 + n4

    print("A^2 = ", n2)
    print("B^2 = ", n4)
    print("C^2 = ", n5)

    n6 = math.sqrt(n5)
    print("Side C = ", n6)

elif SideB > 2:
    m=int(input("Enter the length of side A: "))
    m2 = m**2
    m3=int(input("Enter the length of side C: "))
    m4 = m3**2
    m5 = m4 - m2
    print("A^2 = ", m2)
    print("C^2 = ", m4)
    print("B^2 = ", m5)
    m6 = math.sqrt(m5)
    print("Side B = ", m6)

elif SideA > 2:
    u=int(input("Enter the length of side B: "))
    u2 = u**2
    u3=int(input("Enter the length of side C: "))
    u4 = u3**2
    u5 = u4 - u2
    print("B^2 = ", u2)
    print("C^2 = ", u4)
    print("A^2 = ", u5)
    u6 = math.sqrt(u5)
    print("Side A = ", u6)

else:
    os._exit(0)
















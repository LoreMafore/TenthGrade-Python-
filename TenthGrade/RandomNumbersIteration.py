import random


# Intialize variables we are going to use
Number2 = 0
Number3 = 0
Number4 = 0
Number5 = 0
Number6 = 0
Number7 = 0
Number8 = 0
Number9 = 0
Number10 = 0
Number11 = 0
Number12 = 0
UnitsOfMeasure = 1
Div = "  |  "

# Repeat the imput statement until we get a valid response from the user
while True:
    try:
        MaxIteration = int(input("Enter the maxium number of iterations that " +
                                 "are to be executed (1 to 1000): "))
        if 1 <= MaxIteration <= 1000:
            break
        else:
            print ("INVALID: Enter an integer in the range from 1 to 100.   ",
                   "Please try again...\n", sep="")
    except:
        print ("INVALID: Only intergers are allowed as an input.   ",
               "Please try again...\n", sep="")
        continue

print("")
# Loop through all iteration until it reaches MaxIteration
for Iteration in range(MaxIteration):
    #Generation the random intergers
    Value1 = random.randint(1,6)
    Value2 = random.randint(1,6)
    ValueSum = Value1 + Value2
    #Compare the value and increment appliable counter variable by 1
    
    if ValueSum == 2:
        Number2 = Number2 + 1
    if ValueSum == 3:
        Number3 = Number3 + 1
    if ValueSum == 4:
        Number4 = Number4 + 1
    if ValueSum == 5:
        Number5 = Number5 + 1
    if ValueSum == 6:
        Number6 = Number6 + 1
    if ValueSum == 7:
        Number7 = Number7 + 1
    if ValueSum == 8:
        Number8 = Number8 + 1
    if ValueSum == 9:
        Number9 = Number9 + 1
    if ValueSum == 10:
        Number10 = Number10 + 1
    if ValueSum == 11:
        Number11 = Number11 + 1
    if ValueSum == 12:
        Number12 = Number12 + 1
    #Print the iteration line; broken up for ease of reading
    #Remember that iteration variable will start 0, so add 1 for display
    print ("Iteration: %4s"  %(Iteration + 1), Div,
           "Value1: %1s" %Value1, Div,
           "Value2: %1s" %Value2, Div,
           "SumOfValues: %2s" %ValueSum, sep="")

# Calculate the results
Number2Percent = Number2/MaxIteration*100.0
Number3Percent = Number3/MaxIteration*100.0
Number4Percent = Number4/MaxIteration*100.0
Number5Percent = Number5/MaxIteration*100.0
Number6Percent = Number6/MaxIteration*100.0
Number7Percent = Number7/MaxIteration*100.0
Number8Percent = Number8/MaxIteration*100.0
Number9Percent = Number9/MaxIteration*100.0
Number10Percent = Number10/MaxIteration*100.0
Number11Percent = Number11/MaxIteration*100.0
Number12Percent = Number12/MaxIteration*100.0
Number2Units = int(Number2Percent // UnitsOfMeasure)
if Number2Percent % UnitsOfMeasure > 0:
    Number2Units += 1

Number3Units = int(Number3Percent // UnitsOfMeasure)
if Number3Percent % UnitsOfMeasure > 0:
    Number3Units += 1
Number4Units = int(Number3Percent // UnitsOfMeasure)
if Number4Percent % UnitsOfMeasure > 0:
    Number4Units += 1
Number5Units = int(Number3Percent // UnitsOfMeasure)
if Number5Percent % UnitsOfMeasure > 0:
    Number5Units += 1
Number6Units = int(Number3Percent // UnitsOfMeasure)
if Number6Percent % UnitsOfMeasure > 0:
    Number6Units += 1
Number7Units = int(Number3Percent // UnitsOfMeasure)
if Number7Percent % UnitsOfMeasure > 0:
    Number7Units += 1
Number8Units = int(Number3Percent // UnitsOfMeasure)
if Number8Percent % UnitsOfMeasure > 0:
    Number8Units += 1
Number9Units = int(Number3Percent // UnitsOfMeasure)
if Number9Percent % UnitsOfMeasure > 0:
    Number9Units += 1
Number10Units = int(Number3Percent // UnitsOfMeasure)
if Number10Percent % UnitsOfMeasure > 0:
    Number10Units += 1
Number11Units = int(Number3Percent // UnitsOfMeasure)
if Number11Percent % UnitsOfMeasure > 0:
    Number11Units += 1
Number12Units = int(Number3Percent // UnitsOfMeasure)
if Number12Percent % UnitsOfMeasure > 0:
    Number12Units += 1

#Display the results
print ("\nRESULTS")
print ("[ 2]: ", "%3s" %Number2,
       "  (%6.2f" %Number2Percent, "%)",Div,sep="", end="")
print ("=" * Number2Units)
print ("[ 3]: ", "%3s" %Number3,
       "  (%6.2f" %Number3Percent, "%)",Div,sep="", end="")
print ("=" * Number3Units)
print ("[ 4]: ", "%3s" %Number4,
       "  (%6.2f" %Number4Percent, "%)",Div,sep="", end="")
print ("=" * Number4Units)
print ("[ 5]: ", "%3s" %Number5,
       "  (%6.2f" %Number5Percent, "%)",Div,sep="", end="")
print ("=" * Number5Units)
print ("[ 6]: ", "%3s" %Number6,
       "  (%6.2f" %Number6Percent, "%)",Div,sep="", end="")
print ("=" * Number6Units)
print ("[ 7]: ", "%3s" %Number7,
       "  (%6.2f" %Number7Percent, "%)",Div,sep="", end="")
print ("=" * Number7Units)
print ("[ 8]: ", "%3s" %Number8,
       "  (%6.2f" %Number8Percent, "%)",Div,sep="", end="")
print ("=" * Number8Units)
print ("[ 9]: ", "%3s" %Number9,
       "  (%6.2f" %Number9Percent, "%)",Div,sep="", end="")
print ("=" * Number9Units)
print ("[ 10]: ", "%3s" %Number10,
       "  (%6.2f" %Number10Percent, "%)",Div,sep="", end="")
print ("=" * Number10Units)
print ("[ 11]: ", "%3s" %Number11,
       "  (%6.2f" %Number11Percent, "%)",Div,sep="", end="")
print ("=" * Number11Units)
print ("[ 12]: ", "%3s" %Number12,
       "  (%6.2f" %Number12Percent, "%)",Div,sep="", end="")
print ("=" * Number12Units)

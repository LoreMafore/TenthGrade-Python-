import random

# Display the program header; mine is more than is needed
print ("""
This program is a demonstration of the use of lists and other
variable to make the program more dynamic with regards to
the scope of the test runs.
""")

# Intialize variables we are going to use
Numbers = []   # Notice that we are using a list now, not individual variables
Count = 0      # The count of occurrence is in the second spot in Numbers list
Percent = 1    # The percentage of occurrences is in the second spot in Numbers list
Units = 2      # The unit count is in the third spot in Numbers list
UnitsOfMeasure = 0.5
Div = "  |  "  # There are TWO spaces before and after the delimeter

# Repeat the input statement untill we get a valid response from the userf
while True:
    try:
        MaxIteration = int(input("Enter the maxium number of iterations that " +
                                 "are to be executed (1 to 10000): "))
        if 1 <= MaxIteration <= 10000:
            break
        else:
            print ("INVALID: Enter an integer in the range from 1 to 100.   ",
                   "Please try again...\n", sep="")
    except:
        print ("INVALID: Only intergers are allowed as an input.   ",
               "Please try again...\n", sep="")
        continue
    
while True:
    try:
        MaxInteger = int(input("Enter the maxium number of iterations in " +
                                 "the range (1 to 20): "))
        if 1 <= MaxInteger <= 20:
            break
        else:
            print ("INVALID: Enter an integer in the range from 1 to 20.   ",
                   "Please try again...\n", sep="")
    except:
        print ("INVALID: Only intergers are allowed as an input.   ",
               "Please try again...\n", sep="")
        continue

for Number in range(2,(MaxInteger*2)+1):   # This range covers all possible outcomes
    Numbers.append([0,0,0])      # Initializing my numbers array

print("")
# Loop through all iteration until it reaches MaxIteration
for Iteration in range(MaxIteration):
    # Generate the random integers
    Value1 = random.randint(1,MaxInteger)
    Value2 = random.randint(1,MaxInteger)
    ValueSum = Value1 + Value2
    # Increment appliable counter variable by 1
    Numbers[(ValueSum-2)][Count] +=1
    # Print the iteration line; broken up for ease of reading
    # Remeber that iteration variable will start at 0, so add 1 for display
    print ("Iteration: %5s" %(Iteration + 1), Div,
           "Value1: %2s" %Value1, Div,
           "Value2: %2s" %Value2, Div,
           "SumOfValues: %2s" %ValueSum, sep="")

#Calculate the results
Number = 0
for Item in Numbers:
    # Calculate all of of the percent values in the list
    Numbers[Number][Percent] = (Numbers[Number][Count])/MaxIteration*100.0
    # Calculate all of of the units of measure in the list
    Numbers [Number][Units] = int((Numbers[Number][Percent]) // UnitsOfMeasure)
    # Add 1 to the units of measure if there is a fractional part of the unit
    if (Numbers[Number][Percent]) % UnitsOfMeasure > 0:
        Numbers[Number][Units] += 1
    Number += 1

# Display the results
print ("\nRESULTS")
Number = 0
for Item in Numbers:
    print ("[%2s]: " %(Number+2), "%4s" %Numbers[Number][Count],
           " (%6.2f" %Numbers[Number][Percent], "%)",Div,sep="", end="")
    print ("=" * Numbers[Number][Units])
    Number +=1




    







import os
import random
play = "yes"

print("Hello! I'm your computer. What is your name?")
user_name = input()

print("\nWell, " + user_name + ", I would like to play a number guessing game.")

print ("Please, think of a number between 1 and 100. I am about to try to guess it in 10 tries.")
while play == "yes":
    a = int(input("\nLevel diffuculty 1-10:"))
    if a == 1:
        NumOfTry = 10
    elif a == 2:
        NumOfTry = 9
    elif a == 3:
        NumOfTry = 8
    elif a == 4:
        NumOfTry = 7
    elif a == 5:
        NumOfTry = 6
    elif a == 6:
        NumOfTry = 5
    elif a == 7:
        NumOfTry = 4
    elif a == 8:
        NumOfTry = 3
    elif a == 9:
        NumOfTry = 2
    elif a == 10:
        NumOfTry = 1
    else:
        print ("Not a level")
        os._exit(0)
        
        
    
    NumToGuess = random.randint(1,100)
    LimitLow = 1
    LimitHigh = 100
    while NumOfTry != 0:
        try:
            print ("\nI try: ",NumToGuess)
            print ("Please type: 1 for my try is too high")
            print ("             2 for my try is too low")
            print ("             3 I guessed your number")
            HumanAnswer = int(float(input("\nSo did I guess it right?  Your response: ")))
            if not(1 <= HumanAnswer <= 3):
                print ("\nPlease enter a valid answer. 1, 2 and 3 are valid choices.")
            if HumanAnswer == 1:
                LimitHigh = NumToGuess
                print ("\nHmm, so your number is between ", LimitLow,"and ", LimitHigh)
                NumOfTry = NumOfTry - 1
                print (NumOfTry, "attempts left")
                NumToGuess = int (((LimitHigh - LimitLow)/2) + LimitLow)
                if NumToGuess <= LimitLow:
                    NumToGuess = NumToGuess + 1
                if LimitHigh - LimitLow == 2:
                    NumToGuess = LimitLow + 1
            elif HumanAnswer == 2:
                LimitLow = NumToGuess
                print ("\nHmm, so is your number is between ",LimitLow, "and ", LimitHigh)
                NumOfTry = NumOfTry - 1
                print (NumOfTry, "attempts left")
                NumToGuess = int (((LimitHigh - LimitLow)/2) + LimitHigh)
                if NumToGuess <= LimitLow:
                    NumToGuess = NumToGuess + 1
                if LimitHigh - LimitLow == 2:
                    NumToGuess = LimitLow + 1
            elif HumanAnswer == 3:
                print ("\nWOO HOO! I won!")
                NumOfTry = 0
            
        except:
            print("\nThat's not even a number!")
            continue
    else:
        if NumOfTry == 0 and HumanAnswer !=3:
            print ("\nLooks like you win this time!")

        print ("Do you want to play again? (yes/no)")
        play = input ().lower()

else:
    print("\nThank you for playing",user_name + ".")


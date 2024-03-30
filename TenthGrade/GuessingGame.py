print("Hello! I'm your computer. What is your name? ")
user_name = input()

def main():

    import random 
    import os

        
    print("\nWell, " + user_name + ", I would like to play a number guessing game. Those who don't follow rules will stop playing.") 
    computer_number = random.randint(1, 20)

    print("\nPick level difficulty 1-6")
    level=int(input("\nThe level difficulty is: "))

    if level == 1:
        guess_count = 0
        guess_max = 6

    elif level == 2:
         guess_count = 0
         guess_max = 5
         
    elif level == 3:
         guess_count = 0
         guess_max = 4

    elif level == 4:
         guess_count = 0
         guess_max = 3

    elif level == 5:
         guess_count = 0
         guess_max = 2

    elif level == 6:
         guess_count = 0
         guess_max = 1

    elif level > 6:
         print("GAME OVER")
         os._exit(0)
        
    else:
         level > 1
         print("GAME OVER")
         os._exit(0)

    print("I am thinking of a number between 1 and 20.")

    while guess_count < guess_max: 
        print("\nYou have", (guess_max - guess_count),"guess(es) left.\nWhat is your guess of my number?") 
        guess_value = input() 
        guess_value = int (guess_value) 
        guess_count = guess_count + 1 

        if guess_value < computer_number: 
            print("Your guess is to low.") 

        if guess_value > computer_number:    
            print('Your guess is too high.')  

        if guess_value == computer_number: 
            break  
        if guess_value > 20:
            print("GAME OVER")
            os._exit(0)
        if guess_value < 1:
            print("GAME OVER")
            os._exit(0)

    if guess_value == computer_number: 
        guess_count = str(guess_count)
        print("Congratulations, " 
              + user_name 
              + "!  You guessed my number in  " 
              + guess_count 
              + " guesses!" 
              )  

    if guess_value != computer_number: 
        computer_number = str(computer_number)
        print("GAME OVER! I win! The number i was thinking of was " + computer_number)

    print("\nThank you for playing with me,",user_name + ".")

    restart=input("Do you want to start again: ").lower()
    if restart == "yes" :
        main()

    else:
        os._exit(0)
     
        
main()
    




 

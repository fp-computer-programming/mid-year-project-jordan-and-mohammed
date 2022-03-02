#importing modules/libraries
from random import randint
import random
import time

#Game 
print("-----------------------------------------------------------------------------------------------------")
print("\t""\t""\t""\t""\t""HIGHER AND LOWER WITH A TWIST""\t""\t""\t""\t""\t""\t""\t""\t""\t""\t")
print("-----------------------------------------------------------------------------------------------------")

#FUNCTION FOR GAME INFO
def instruction():
    #Game Instructions
    print("INSTRUCTIONS")
    print("---------------------")
    print("\t""""The objective of the game is to guess the correct number the system will indicate you if your
    guessed number is higher or lower""")

    print("-----------------------------------------------------------------------------------------------------")
    print("\t""\t""\t""\t""\t""PLAYER PROFILE")
    print("-----------------------------------------------------------------------------------------------------")
    
# FUNCTION FOR PLAYER PROFILE
def profile():
    #Taking User Input
    name = input("Enter your Name: ")
    print()
    print("Hello",name.upper(),".")
    
# FUNCTION FOR MAIN GAME
def game():
    print("_____________________________________________________________________________________________________")
    print("\t""\t""\t""\t""\t""LET THE GAME BEGIN")
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print()
    print("Guess between number 1 to 100 ""\n""You have 8 chances to guess the number")
    print()
    
     #GENERATING RANDOM NUMBER
    num = randint (1,100)
    
    #VARIABLE
    tries=8
    
    #WHILE LOOP
    while tries!=0:
        
        guess = int(input("Make your guess: "))
        
        #APPLYING LOGIC THROUGH CONDITIONS
        if guess > num:
            print("Lower")
            tries = tries - 1
            print()
                
        elif guess < num:
            print("Higher")
            tries = tries - 1
            print()
        else:
            print("------------------------")
            print("Your guess is correct.")
            print("------------------------")
            print()
            again()
        
        #CONDITION FOR A HANGMAN
        if tries == 8 :
            print("Wrong Answer")
            time.sleep(1)
            print(" 8 turns left")
            print("-------------")
            print("      O      ")
                
        if tries == 7 :
            print("Wrong Answer")
            time.sleep(1)
            print(" 7 turns left")
            print("-------------")
            print("      O      ")   
            print("      |      ")
                
        if tries == 6 :
            print("Wrong Answer")
            time.sleep(1)
            print(" 6 turns left")
            print("-------------")
            print("      O      ")   
            print("      |      ")   
            print("     /       ")
                
        if tries == 5 :
            print("Wrong Answer")
            time.sleep(1)
            print(" 5 turns left")
            print("-------------")
            print("      O      ")   
            print("      |      ")   
            print("     / \     ")
            print("             ")
            
        if tries == 4 :
            print("Wrong Answer")
            time.sleep(1)
            print(" 4 turns left")
            print("-------------")
            print("     \O      ")   
            print("      |      ")   
            print("     / \     ")
            print("             ")
            
        if tries == 3 :
            print("Wrong Answer")
            time.sleep(1)
            print(" 3 turns left")
            print("-------------")
            print("     \O/   | ")   
            print("      |      ")   
            print("     / \     ")
            print("             ")
                     
        if tries == 2 :
            print("Wrong Answer")
            time.sleep(1)
            print(" 2 turns left")
            print("-------------")
            print("     \O/  _| ")   
            print("      |      ")   
            print("     / \     ")
            print("             ")
                
        if tries == 1 :
            print("Wrong Answer")
            time.sleep(1)
            print(" 1 turns left")
            time.sleep(1)
            print("Not much life lefts!!")
            print("-------------")
            print("     \O/_|   ")   
            print("      |      ")   
            print("     / \     ")
            print("             ")
                
        if tries == 0 :
            print("Wrong Answer, You Lost")
            time.sleep(1)
            print(" 0 turns left")
            print("R.I.P \U0001F62A !!!")
            print("-------------")
            print("      |      ")
            print("      |      ")
            print("      O      ")   
            print("     /|\     ")   
            print("     / \     ")
            print("             ")
            time.sleep(1)
            
            #DECLARING THE ACTUAL NUMBER
            print("---------------------------")
            print("The Correct number is",num)
            print("---------------------------")
            again()

#ASKING FOR A RESET(TO PLAY AGAIN)
def again():
    ask = input("Do you wish to play again? y/n: ")
    if ask=="y":
        game()
    elif ask=="n":
        exit()
    else:
        exit()
    
instruction()
profile()
game()

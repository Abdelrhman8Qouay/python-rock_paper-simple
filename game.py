import random
import os
import re

#====>>> static program
# list_game = ['rock', 'paper', 'scissors']

# def startGame():
#     who_win = 0
#     chosePC = random.randint(0, len(list_game))
#     serPC = list_game[chosePC].lower()

#     while True:
#         try:
#             choseUser = str(input("choose between [R]ock or [P]aper or [S]cissors: "))

#             ser = re.match(f"{choseUser}|^{choseUser[0]}", ' '.join(list_game), re.I)
#             if not ser:
#                 print("your text is not valid, try again")
#                 break

#             print(f"I Chose: {serPC}")
#             print(f"You Chose: {ser[0]}")

#             #// the condition to know who won
#             if ser[0].lower() == "paper" and serPC == "rock": who_win = 1
#             if ser[0].lower() == "p" and serPC == "rock": who_win = 1
#             if ser[0].lower() == "paper" and serPC == "scissors": who_win = 2
#             if ser[0].lower() == "p" and serPC == "scissors": who_win = 2
#             if ser[0].lower() == "rock" and serPC == "paper": who_win = 2
#             if ser[0].lower() == "r" and serPC == "paper": who_win = 2
#             if ser[0].lower() == "rock" and serPC == "scissors": who_win = 1
#             if ser[0].lower() == "r" and serPC == "scissors": who_win = 1
#             if ser[0].lower() == "scissors" and serPC == "rock": who_win = 2
#             if ser[0].lower() == "s" and serPC == "rock": who_win = 2
#             if ser[0].lower() == "scissors" and serPC == "paper": who_win = 1
#             if ser[0].lower() == "s" and serPC == "paper": who_win = 1

#             if ser[0].lower() == serPC: who_win = 3
#             if ser[0][0].lower() == serPC[0]: who_win = 3

#             if who_win == 1:
#                 print("So, You win ^_^")
#                 #//wanna play again
#                 wanna_play = input("Do you wanna play again? Enter(Yes/No): ")
#                 if wanna_play.lower() != "yes":
#                     print("Okay, GoodLuck!.")
#                     break
#                 else:
#                     chosePC = random.randint(0, len(list_game))
#                     os.system('cls' if os.name == 'nt' else 'clear')
#                     continue
#             elif who_win == 2:
#                 print("So, You Lose :(")
#                 #//wanna play again
#                 wanna_play = input("Do you wanna play again? Enter(Yes/No): ")
#                 if wanna_play.lower() != "yes":
#                     print("Okay, GoodLuck!.")
#                     break
#                 else:
#                     chosePC = random.randint(0, len(list_game))
#                     os.system('cls' if os.name == 'nt' else 'clear')
#                     continue
#             elif who_win == 3:
#                 print("So, No one Win (")
#                 chosePC = random.randint(0, len(list_game))
#                 continue
#         except:
#             print("the except containing an error from try")

# if __name__ == '__main__':
#     print("Let's start to play the game ^_@")
#     startGame()

#// program ===>>>>> more advanced
list_game = ['rock', 'paper', 'scissors']

def check_play_status():
    valid_res = ['yes', 'no']
    while True:

        try:

            wanna_play = input("Do you wanna play again? Enter(Yes/No): ")
            if wanna_play.lower() not in valid_res:
                raise ValueError("I can't Understand You..., Yes or No? :(")

            if wanna_play.lower() == "no":
                print("Okay, GoodLuck!.")
                exit()
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                return True

        except ValueError as err:
            print(err)


def startGame():
    who_win = 0

    play = True
    while play:
        chosePC = random.randint(0, len(list_game) - 1)
        serPC = list_game[chosePC].lower()

        choseUser = input("choose between [R]ock or [P]aper or [S]cissors: ")

        ser = re.search(f"{choseUser}|^{choseUser[0]}", ' '.join(list_game), re.I)
        if not ser:
            print("You chose something out... Not Valid Do This.")
            break

        print(f"I Chose: {serPC}")
        print(f"You Chose: {ser.group()}")

            #// the condition to know who won
        if ser[0].lower() == "paper" and serPC == "rock": who_win = 1
        if ser[0].lower() == "p" and serPC == "rock": who_win = 1
        if ser[0].lower() == "paper" and serPC == "scissors": who_win = 2
        if ser[0].lower() == "p" and serPC == "scissors": who_win = 2
        if ser[0].lower() == "rock" and serPC == "paper": who_win = 2
        if ser[0].lower() == "r" and serPC == "paper": who_win = 2
        if ser[0].lower() == "rock" and serPC == "scissors": who_win = 1
        if ser[0].lower() == "r" and serPC == "scissors": who_win = 1
        if ser[0].lower() == "scissors" and serPC == "rock": who_win = 2
        if ser[0].lower() == "s" and serPC == "rock": who_win = 2
        if ser[0].lower() == "scissors" and serPC == "paper": who_win = 1
        if ser[0].lower() == "s" and serPC == "paper": who_win = 1

        if ser[0].lower() == serPC: who_win = 3
        if ser[0][0].lower() == serPC[0]: who_win = 3

        if who_win == 1:
            print("So, You win ^_^")
            chosePC = random.randint(0, len(list_game) - 1)
            play = check_play_status()
        elif who_win == 2:
            print("So, You Lose :(")
            chosePC = random.randint(0, len(list_game) - 1)
            play = check_play_status()
        elif who_win == 3:
            print("So, No one Win (, Try again.")
            chosePC = random.randint(0, len(list_game) - 1)
            continue
        else:
            print("something happend with how win")

if __name__ == '__main__':
    print("Let's start to play the game ^*^")
    startGame()

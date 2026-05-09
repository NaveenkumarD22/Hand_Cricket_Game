"""
Requirements:
1) Toss to be implemented

"""


# Start of program
from os import system
import time
import random as rd


def scroll(a):
    for i in range(50):
        _ = system('cls')
        print((" " * i) + a)
        time.sleep(0.1)


def print_banner():
    print("WELCOME TO THE GAME OF HAND-CRICKET!")
    print("------------------------------------")


def toss_check():
    odd_or_even_choice = input("Now choose either odd or even: ")
    while not(odd_or_even_choice == "odd" or odd_or_even_choice == "even"):
        odd_or_even_choice = input("Kindly choose ONLY EITHER of odd OR even: ")
    
    toss_userchoice = input("Now enter a number from 1 to 10 as your choice for the toss: ")
    choice_list = ['1','2','3','4','5','6','7','8','9','10']
    while not(toss_userchoice in choice_list):
        toss_userchoice = input("Kindly enter numbers from 1 to 10 ONLY as your choice for the toss: ")
    toss_userchoice = int(toss_userchoice)
    toss_botchoice = int(rd.choice(choice_list))

    print("For the toss, YOU have chosen '", odd_or_even_choice, "' and '", toss_userchoice, "'.", sep = '')
    print("For the toss, BOT has chosen '", toss_botchoice, "'.", sep = '')

    if (toss_userchoice + toss_botchoice) % 2 == 0:
        odd_or_even = "even"
    else:
        odd_or_even = "odd"
    print(odd_or_even)
    if odd_or_even == odd_or_even_choice:
        toss_winner = "Player(You)"
    else:
        toss_winner = "Bot" 
    return toss_winner



scroll("WELCOME TO THE GAME OF HAND-CRICKET!")
_ = system('cls')
print_banner()
toss_winner = toss_check()
if toss_winner == "Player(You)":
    print("Congrats! You have won the toss!")
    toss = input("Do you choose to bat or bowl? : ")
    while not(toss == 'bat' or toss == 'bowl'):
        toss = input("Kindly check your spelling and enter only 'bat' or 'bowl': ")
    if toss == "bat":
        batter = "Player"
    else:
        batter = "Bot"
else:
    print("Unlucky, the BOT has won the toss.")
    toss = rd.choice("bat", "bowl")
print("Alright!", toss_winner,"has/have won the toss and chosen to", toss)
print("NOW LET THE GAME BEGIN!!!")

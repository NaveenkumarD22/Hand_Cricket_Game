'''
Requirements:
1) Print banner to be finished with controls of the game, instructions etc.
2) Full game logic to be finished
'''

#Start of program
from os import system
import time
import random as rd


def scroll(a):
    for i in range(50):
        _ = system('cls')
        print((" " * i) + a)
        time.sleep(0.1)


def print_banner():
    print("\033[4m" + "WELCOME TO THE GAME OF HAND-CRICKET!" + "\033[0m")
    print("")
    print("Game Instructions:")
    print("1) Similar to cricket, there are two teams playing against each other across TWO INNINGS,", end = " ")
    print("switching from bowling to batting and vice versa in the second inning.")
    print()

    print("2) In the SECOND inning, the bowler in the first inning must chase and OVERSCORE the runs scored", end = " ")
    print("by the batter in the FIRST inning.", end = " ")
    print("If he does so, he is deemed as the WINNER. If he doesn't manage to, then the OTHER player is deemed as the WINNER.")
    print()

    print("3)In the rare case where in the second inning, the batter is only able to score the EXACT SAME NUMBER OF RUNS", end = " ")
    print("as the other player in the first inning before getting out, then the match is considered a DRAW.")
    print()

    print("4) You will be playing against the COMPUTER(BOT). Each turn, both of you will be choosing a number from one to ten.", end = " ")
    print("If both of you keep the SAME number, then the batter is OUT, and the runs he/she/it scored till that will be made to be chased by the other player in the SECOND inning,", end = " ")
    print("or the match gets OVER if it is ALREADY the second inning.")
    print()

    print("5) If both of you choose DIFFERENT numbers, then the number entered by the batter will be added to the batter's score.")
    print()

    print("6) For the TOSS, you will be asked to choose either 'odd' or 'even' and both of you will be entering a number from one to ten.", end = " ")
    print("If the SUM of two numbers that both of you entered is as per your choice(odd/even), then you WIN the toss", end = " ")
    print("and you will be asked to BAT or BOWL for the first inning. If you don't win the toss, then the computer AUTOMATICALLY WINS it and gets to choose to bat or bowl.")
    print()


def toss_check():
    odd_or_even_choice = input("Now, for the TOSS, choose either odd or even: ")
    while not(odd_or_even_choice == "odd" or odd_or_even_choice == "even"):
        odd_or_even_choice = input("Kindly choose ONLY EITHER of odd OR even: ")
    
    toss_userchoice = input("Now enter a number from 1 to 10 as your choice for the toss: ")
    toss_choice_list = ['1','2','3','4','5','6','7','8','9','10']
    while not(toss_userchoice in toss_choice_list):
        toss_userchoice = input("Kindly enter numbers from 1 to 10 ONLY as your choice for the toss: ")
    toss_userchoice = int(toss_userchoice)
    toss_botchoice = int(rd.choice(toss_choice_list))

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


def score_banner(innings, score, chase, batter, bowler):
    print()
    print("Innings: ", innings)
    print("Batter: ", batter, end = "       ")
    print("Bowler: ", bowler)
    if innings == 2:
        print("Current runs: ", score, end = "     ")
        print("Runs to chase: ", chase - score)
    else:
        print("Current runs: ", score)
        

def win_check(score, chase, batter, bowler):
    if score >= chase:
        winner = batter
    else:
        if score == chase - 1:
            winner = "None"
        else:
            winner = bowler
    return winner


def inning1_over(score, chase, batter, bowler):
    print()
    print("It's an OUT!")
    print("With that the first inning ends.", end = "\n\n")
    print(batter, "has scored", score, "runs.", end = " ")
    print("Now, in the second inning,", bowler, "has to score", chase, "run(s) to win.")
    print("With that, let the second inning begin!")
    _ = input("(enter any key to continue)")
    _ = system('cls')


def outro_printbanner(winner, batter, bowler, score, chase):
    pass


# Start of Main program
scroll("WELCOME TO THE GAME OF HAND-CRICKET!")
_ = system('cls')
print_banner()
toss_winner = toss_check()
if toss_winner == "Player(You)":
    print("CONGRATS! You have won the toss!")
    toss = input("Do you choose to bat or bowl? : ")
    while not(toss == 'bat' or toss == 'bowl'):
        toss = input("Kindly check your spelling and enter only 'bat' or 'bowl': ")
    if toss == "bat":
        batter,bowler = "Player","Bot"
    else:
        batter,bowler = "Bot","Player"
else:
    print("UNLUCKY, the BOT has won the toss.")
    toss = rd.choice(['bat','bowl'])
    if toss == "bat":
        batter,bowler = "Bot","Player"
    else:
        batter,bowler = "Player","Bot"
print("Alright!", toss_winner,"has/have won the toss and chosen to", toss)
print()
print("NOW LET THE GAME BEGIN!!!")
_ = input("(enter any key to start)")
_ = system('cls')

score = 0
innings = 1
chase = 1

while not(innings > 2 or score >= chase):
    score_banner(innings, score, chase, batter, bowler)
    user_choice = input("Enter a number from 1 to 10: ")
    choice_list = ['1','2','3','4','5','6','7','8','9','10']
    while not(user_choice in choice_list):
        user_choice = input("Kindly enter numbers from 1 to 10 ONLY: ")
    user_choice = int(user_choice)
    #bot_choice = rd.choice(choice_list)
    bot_choice = 7
    bot_choice = int(bot_choice)
    print("The bot has chosen", bot_choice)

    if user_choice == bot_choice:
        if innings == 1:
            chase = score + 1
            inning1_over(score, chase, batter, bowler)
            score = 0
            innings = 2
            batter,bowler = bowler,batter
        else:
            break

    else:
        if batter == "Player":
            score += user_choice
        else:
            score += bot_choice
        if innings == 1:
            chase = score + 1

winner = win_check(score, chase, batter, bowler)
outro_printbanner(winner, batter, bowler, score, chase)

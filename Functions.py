import random
import pandas as pd
final_string = ""
choicegesture = 0
gesturelist = ""
number_of_gesture = 0
ROCK = 0
PAPER = 1
SCISSORS = 2 
SPOCK = 3
LIZARD = 4
AIR = 5 
FIRE = 6 
HUMAN = 7 
GUN = 8 
WOLF = 9 
DEVIL = 10 
PLAYERS = 2
SERIESWINNER = 2 
SUCCESS = 0
FAILURE = 1
ROCKSTRING ="Rock"
PAPERSTRING = "Paper"
SCISSORSSTRING = "Scissors"
SPOCKSTRING = "Spock"
LIZARDSTRING = "Lizard"
AIRSTRING = "Air"
FIRESTRING = "Fire"
HUMANSTRING = "Human"
GUNSTRING = "Gun"
WOLFSTRING = "Wolf"
DEVILSTRING = "Devil"
PLAYER = 1
COMPUTER = -1
TIE = 0
ERROR = 3
player_score = 0
computer_score = 0
game_count = 0
computer_gesture = 0
human_gesture = 0
game_winner = 0
human = 0
computer = 0


def get_gesture(number_of_gesture):
    final_string = ""
    choicegesture = [
                                "Enter 0 for rock, 1 for paper, 2 for scissors", 
                                "3 for spock, 4 for lizard",
                                "5 for air, 6 for fire",
                                "7 for human, 8 for gun",
                                "9 for wolf, 10 for devil"
                        ]
    print("Please enter your gesture")
    x = int((number_of_gesture-1)/2)
    for i in range(x):
        if (i<x):
            final_string = (final_string + choicegesture[i])
    c = int(input(final_string))
    return(c)

def check_gesture(gesture,number_of_gesture):
    i = 0
    gesturelist = [ROCK, PAPER, SCISSORS, SPOCK, LIZARD, AIR, FIRE, HUMAN, GUN, WOLF, DEVIL]
    for i in range(len(gesturelist)):
        if (gesture == gesturelist[i]):
            return SUCCESS
    return FAILURE

def display_choice(a):
      if a == ROCK:
           return ROCKSTRING
      elif a == PAPER:
           return PAPERSTRING
      elif a == SCISSORS:
            return SCISSORSSTRING
      elif a == SPOCK:
             return SPOCKSTRING
      elif a == LIZARD:
              return LIZARDSTRING
      elif a == AIR:
              return AIRSTRING
      elif a == FIRE:
               return FIRESTRING
      elif a == HUMAN:
               return HUMANSTRING
      elif a == GUN:
           return GUNSTRING
      elif a == WOLF:
            return WOLFSTRING
      else: 
             return DEVILSTRING
     
        

        
def show_game_winner(inputwinner):
    if (inputwinner == TIE):
        print("It's a tie!")
    elif (inputwinner == PLAYER):
        print("You win!")
    else:
        print("Computer wins!")

def show_series_winner(input_player_score, input_computer_score):
    if (input_player_score == SERIESWINNER):
        print("You won the series")
    elif (input_computer_score == SERIESWINNER):
        print("The computer won the series")
def determine_game_winner(computer, human, number_of_gesture):
    i = 0
    ii = 0
    if(computer==human):
        return(TIE)
    winners = [
                [ROCK,SCISSORS, LIZARD, FIRE, HUMAN, WOLF], 
                [PAPER, ROCK, SPOCK, AIR, GUN, DEVIL], 
                [SCISSORS, PAPER, LIZARD, AIR, HUMAN, WOLF],
                [SPOCK, ROCK, SCISSORS, FIRE, GUN, DEVIL], 
                [LIZARD, PAPER, SPOCK, AIR,GUN, DEVIL],
                [AIR, ROCK, SPOCK, FIRE, GUN, DEVIL],
                [FIRE,ROCK, SCISSORS, FIRE, GUN, DEVIL],
                [HUMAN, PAPER, SPOCK, LIZARD, AIR, WOLF],
                [GUN, ROCK, SCISSORS, FIRE, HUMAN, WOLF],
                [WOLF, PAPER, SPOCK, LIZARD, AIR, DEVIL],
                [DEVIL, ROCK, SCISSORS, FIRE, HUMAN, GUN]
    ]
    
    for i in range(number_of_gesture):
        if (computer == winners[i][0]):
            for ii in range((number_of_gesture+1)//2 -1):
                if (human == winners[i][ii]):
                    return (COMPUTER) 
            return (PLAYER)



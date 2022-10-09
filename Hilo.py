import random
import os
 
# Function to clear the terminal
def clear():
    os.system("cls")
 
# Function to print the scorebaord  
def print_scoreboard(score):
    print("\t\t\t    ____________________")
    print("\t\t\t                        ")
    print("\t\t\t         Score = {}     ".format(score))
    print("\t\t\t    ____________________")
 
# Function to print the cards (I found this online!)
def print_cards(prev_card, current_card):
     
    print()
    print("\t ________________      ________________      ________________")
    print("\t|                |    |                |    |                |")
    if prev_card.value == '10' and current_card.value == '10':
        print("\t|  {}            |    |  {}            |    |                |".format(prev_card.value,current_card.value))
    elif prev_card.value == '10': 
        print("\t|  {}            |    |  {}             |    |                |".format(prev_card.value,current_card.value))   
    elif current_card.value == '10':
        print("\t|  {}             |    |  {}            |    |                |".format(prev_card.value,current_card.value))   
    else:
        print("\t|  {}             |    |  {}             |    |                |".format(prev_card.value,current_card.value))  
    print("\t|                |    |                |    |      * *       |")
    print("\t|                |    |                |    |    *     *     |")
    print("\t|                |    |                |    |   *       *    |")
    print("\t|                |    |                |    |   *       *    |")
    print("\t|       {}        |    |       {}        |    |          *     |".format(prev_card.suit, current_card.suit))
    print("\t|                |    |                |    |         *      |")
    print("\t|                |    |                |    |        *       |")
    print("\t|                |    |                |    |                |")
    print("\t|                |    |                |    |                |")
    if prev_card.value == '10' and current_card.value == '10':
        print("\t|            {}  |    |            {}  |    |        *       |".format(prev_card.value,current_card.value))
    elif prev_card.value == '10': 
        print("\t|            {}  |    |            {}   |    |        *       |".format(prev_card.value,current_card.value))   
    elif current_card.value == '10':
        print("\t|            {}   |    |            {}  |    |        *       |".format(prev_card.value,current_card.value))   
    else:
        print("\t|            {}   |    |            {}   |    |        *       |".format(prev_card.value,current_card.value))  
    print("\t|________________|    |________________|    |________________|")
    print()
 
    
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        
class Choice:
    def __init__(self, choice, result):
        self.choice = choice
        self.result = result

def hi_lo_game(deck):
 
    global cards_values
    prev_card = Card(" ", " ")
    current_card = random.choice(deck)
    
    while current_card.value == "A" or current_card.value == "K":
        current_card = random.choice(deck)
        
    deck.remove(current_card)
    
    score = 300

    while score:
 
        print_scoreboard(score)
        print_cards(prev_card, current_card)
 
        print("\t\t   ------------------------------------")
        print("\t\t\t\tGAME MENU")
        print("\t\t   ------------------------------------")
        print()
        print("\t\t      Enter 1 to bet for a high card")
        print("\t\t      Enter 0 to bet for a low card")
        print()
         
        if len(deck) == 0:
            clear()
            print_cards(prev_card, current_card)
            print("\t\t    YOU HAVE REACHED THE END OF THE DECK!")
            print("\t\t           Congratulations!!!")
            print()
            print("\t\t          Your Final Score =", score)
            print("\t\t        Thank you for playing!!!")
            break
 
        try:
            choice = int(input("\t\t\t  Enter your choice = "))
        except ValueError:
            clear()
            print("\t\t\tWrong Input!! Try Again.")
            continue   
 
        if choice > 1 or choice < 0:
            clear()
            print("\t\t\tWrong Input!! Try Again.")
            continue       
 
        prev_card = current_card
        current_card = random.choice(deck)
        deck.remove(current_card)
 
        # A high card
        if cards_values[current_card.value] > cards_values[prev_card.value]:
            result = 1
 
        # A low card    
        elif cards_values[current_card.value] < cards_values[prev_card.value]:
            result = 0
 
        # Same value card   
        else:
            result = -1    
 
        # A Tie Round
        if result == -1:
            clear()
            print("\t\t\t Welp. This is awkward, try again I guess?")
 
        # Round won
        elif choice == result:
            clear()
            print("\t\t\t Good choice! Have some score!")
            score = score + 100 
 
        # Round Lost    
        else:
            if score == 0:
                clear()
                print("\t\t\t\t Sorry homie, try again if you want though!")
                print_cards(prev_card, current_card)
                print("\t\t      Thank you for playing!!!")
                break  
            clear()
            print("\t\t\t Good try, guess again if you want!")
            score = score - 75
 
 
if __name__ == '__main__':
    
    suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
    suits_values = {"Spades":"\u2664", "Hearts":"\u2661", "Clubs": "\u2667", "Diamonds": "\u2662"}
    cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    cards_values = {"A": 1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":11, "Q":12, "K":13}
 
    deck = []

    for suit in suits:
        for card in cards:
            deck.append(Card(suits_values[suit], card))
 
    hi_lo_game(deck)
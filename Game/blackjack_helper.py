# DO NOT CHANGE OR REMOVE THIS COMMENT, and do not change this import otherwise all tests will fail.
from random import randint
# Write all of your part 3 code below this comment. DO NOT CHANGE OR REMOVE THIS COMMENT.

# Prints the given card's official name in the form "Drew a(n) ___".
# If the input card is invalid, prints "BAD CARD"
# 
# Parameters:
#   card_rank: The numeric representation of a card (1-13)
#
# Return:
#   none
def print_card_name(card_rank):
  
  if card_rank == 1:
  # A 1 stands for an ace.
   card_name = "Ace"
  elif card_rank == 11:
  # An 11 stands for a jack.
   card_name = "Jack"
  elif card_rank == 12:
  # A 12 stands for a queen.
   card_name = "Queen"
  elif card_rank == 13:
  # A 13 stands for a king.
   card_name = "King"
  elif card_rank>13:
    card_name = "BAD CARD"
  else:
  # All other cards are named by their number, or rank.
   card_name = str(card_rank)

  if card_rank == 1 or card_rank == 8:
   print('Drew an ' + card_name)    
  elif card_rank>13:
    print(card_name)
  else:
   print('Drew a ' + card_name)

def draw_card():
  card_rank=randint(1,13)  
  print_card_name(card_rank)
  if card_rank == 11 or card_rank == 12 or card_rank == 13:
  # Jacks, Queens, and Kings are worth 10.
   card_value = 10
  elif card_rank == 1:
  # Aces are worth 11.
   card_value = 11
  else:
  # All other cards are worth the same as their rank.
   card_value = card_rank
  return card_value  

def print_header(message):
    print('-----------\n' + message + '\n-----------')

def draw_starting_hand(name):
   print_header(name.upper() + " TURN")
   card_1 = draw_card()
   card_2 = draw_card()
   return card_1 + card_2
def print_end_turn_status(hand_value):
    print("Final hand: " + str(hand_value) + ".")
    if hand_value == 21:
     print("BLACKJACK!")
    elif hand_value > 21:
     print("BUST.")

def print_end_game_status(user_hand, dealer_hand):
    print_header("GAME RESULT")
    if user_hand==21:
        if dealer_hand==21:
            print("Push.")
        elif dealer_hand<21:
            print("You win!")
        elif dealer_hand>21:
            print("You win!")
    elif user_hand==dealer_hand:
        print("Push.")        
    elif user_hand>21:
        if dealer_hand==21:
            print("Dealer wins!")
        elif dealer_hand<21:
            print("Dealer wins!") 
        elif dealer_hand>21:
            print("Dealer wins!")     
    elif user_hand<21:
        if user_hand<dealer_hand<21:
            print("Dealer wins!")
        elif user_hand<dealer_hand:
            print("You win!")
        elif user_hand>dealer_hand<21:
            print("You win!")
        elif dealer_hand==21:
            print("You win!") 

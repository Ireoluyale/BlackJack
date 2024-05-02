# DO NOT CHANGE OR REMOVE THIS COMMENT, and do not change this import otherwise all tests will fail.
from blackjack_helper import *

# Write all of your part 3 code below this comment. DO NOT CHANGE OR REMOVE THIS COMMENT.
#1
user_hand_total = draw_starting_hand("your")
while user_hand_total < 21:
  should_hit = input('You have ' + str(user_hand_total) + ". Hit (y/n)? ")
  if should_hit == 'n':
    break
  elif should_hit == 'y':
    card_value = draw_card()
    user_hand_total = user_hand_total + card_value
  else:
    print("Sorry I didn't get that.")
print_end_turn_status(user_hand_total)
dealer_hand_total = draw_starting_hand("dealer")
while dealer_hand_total < 17:
  card_value = draw_card()
  dealer_hand_total += card_value
  if dealer_hand_total < 17:
      print("Dealer has {}.".format(hand_value))
print_end_turn_status(dealer_hand_total)
print_end_game_status(user_hand_total, dealer_hand_total)

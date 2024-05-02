from blackjack_helper import *
from test_helper import *
import unittest

class TestBlackjackHelper(unittest.TestCase):
  """
  Class for testing blackjack helper functions.
  """

  def test_print_card_name_example(self):
    """
    Example of a test to compare printed statements with expected

    This does not count as one of your tests
    """
    self.assertEqual(get_print(print_card_name, 2), "Drew a 2\n")

  def test_mock_randint_example(self):
    """
    Example of a test to compare output for a function that calls randint

    This does not count as one of your tests
    """
    self.assertEqual(mock_random([3], draw_card), 3)
    self.assertEqual(mock_random([3, 5], draw_starting_hand, "DEALER"), 8)

  # MAKE SURE ALL YOUR FUNCTION NAMES BEGIN WITH test_
  # WRITE YOUR TESTS BELOW.
  def test_print_card_name(self):
    self.assertEqual(get_print(print_card_name, 1), "Drew an Ace\n")
    self.assertEqual(get_print(print_card_name, 99), "BAD CARD\n")
    self.assertEqual(get_print(print_card_name, 13), "Drew a King\n")
  def test_draw_card(self):
    self.assertEqual(mock_random([3], draw_card), 3)
    self.assertEqual(mock_random([13], draw_card), 10)
    self.assertEqual(mock_random([1], draw_card), 11)
  def test_print_header(self):
    self.assertEqual(get_print(print_header,"hi"),"-----------\n{}\n-----------\n".format("hi"))  
    self.assertEqual(get_print(print_header,"csci"),"-----------\n{}\n-----------\n".format("csci"))
    self.assertEqual(get_print(print_header,"message"),"-----------\n{}\n-----------\n".format("message"))
  def test_draw_starting_hand(self):
    output = mock_random([5,6], draw_starting_hand, "DEALER")
    self.assertEqual(output, 11)
    output = mock_random([5,13], draw_starting_hand, "DEALER")
    self.assertEqual(output, 15)
    output = mock_random([5,12], draw_starting_hand, "DEALER")
    self.assertEqual(output, 15)  
  def test_print_end_turn_status(self):
    self.assertEqual(get_print(print_end_turn_status, 10), "Final hand: " + str(10) + ".\n")
    self.assertEqual(get_print(print_end_turn_status, 21), "Final hand: " + str(21) + ".\nBLACKJACK!\n")
    self.assertEqual(get_print(print_end_turn_status, 28), "Final hand: " + str(28) + ".\nBUST.\n")
  def test_print_end_game_status(self):
    self.assertEqual(get_print(print_end_game_status, 16, 21), "-----------\nGAME RESULT\n-----------\nDealer wins!\n")
    self.assertEqual(get_print(print_end_game_status, 21, 31), "-----------\nGAME RESULT\n-----------\nYou win!\n")
    self.assertEqual(get_print(print_end_game_status, 16, 16), "-----------\nGAME RESULT\n-----------\nPush.\n")


if __name__ == '__main__':
    unittest.main()

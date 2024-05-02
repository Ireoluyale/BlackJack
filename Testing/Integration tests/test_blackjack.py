from unittest import TestCase, main
from unittest.mock import patch
from test_helper import run_test

class TestBlackjack(TestCase):

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_example(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards that end up with a hand less than 21.
        The dealer wins by having a higher hand than the user.

        This does not count as one of your tests.
        '''
        output = run_test([3, 5, 8], ['y', 'n'], [3, 5, 10], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "You have 8. Hit (y/n)? y\n" \
                   "Drew an 8\n" \
                   "You have 16. Hit (y/n)? n\n" \
                   "Final hand: 16.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "Dealer has 8.\n" \
                   "Drew a 10\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)

    # Make sure all your test functions start with test_ 
    # Follow indentation of test_example
    # WRITE ALL YOUR TESTS BELOW. Do not delete this line.
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_dealer_win_case_1(self, input_mock, randint_mock):
        #dealer hand<21, user hand<21 but dealer hand>user hand
        output_1 = run_test([3, 5, 8], ['y', 'n'], [3, 5, 10], randint_mock, input_mock)
        expected_result_1 = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "You have 8. Hit (y/n)? y\n" \
                   "Drew an 8\n" \
                   "You have 16. Hit (y/n)? n\n" \
                   "Final hand: 16.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "Dealer has 8.\n" \
                   "Drew a 10\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output_1, expected_result_1)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_win_case_1(self, input_mock, randint_mock):
        #dealer hand<21, user hand<21 but dealer hand<user hand
        output_2 = run_test([3, 5, 8], ['y', 'n'], [3, 5, 2], randint_mock, input_mock)
        expected_result_2 = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "You have 8. Hit (y/n)? y\n" \
                   "Drew an 8\n" \
                   "You have 16. Hit (y/n)? n\n" \
                   "Final hand: 16.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "Dealer has 8.\n" \
                   "Drew a 2\n" \
                   "Final hand: 10.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"
        self.assertEqual(output_2, expected_result_2)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_dealer_win_case_2(self, input_mock, randint_mock):
        #dealer hand<21, user hand>21
        output_3 = run_test([7, 7, 9], ['y','n'], [3, 5, 2], randint_mock, input_mock)
        expected_result_3 = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 7\n" \
                   "Drew a 7\n" \
                   "You have 14. Hit (y/n)? y\n" \
                   "Drew an 9\n" \
                   "Final hand: 23.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "Dealer has 8.\n" \
                   "Drew a 2\n" \
                   "Final hand: 10.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output_3, expected_result_3)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_dealer_win_case_3(self, input_mock, randint_mock):
        #dealer hand>21, user hand>21
        output_4 = run_test([9, 9, 9], ['y','n'], [3, 5, 10], randint_mock, input_mock)
        expected_result_4 = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 9\n" \
                   "Drew a 9\n" \
                   "You have 18. Hit (y/n)? y\n" \
                   "Drew a 9\n" \
                   "Final hand: 27.\n" \
                   "BUST."\
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 9\n" \
                   "Drew a 9\n" \
                   "Dealer has 18.\n" \
                   "Drew a 9\n" \
                   "Final hand: 27.\n" \
                   "BUST."\
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output_4, expected_result_4)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_win_case_2(self, input_mock, randint_mock):
        #dealer hand>21, user hand<21
        output_5 = run_test([9, 9], ['n'], [3, 9, 10], randint_mock, input_mock)
        expected_result_5 = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 9\n" \
                   "Drew a 9\n" \
                   "You have 18. Hit (y/n)? n\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 9\n" \
                   "Dealer has 12.\n" \
                   "Drew a 10\n" \
                   "Final hand: 22.\n" \
                   "BUST."\
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"
        self.assertEqual(output_5, expected_result_5)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_push_case_1(self, input_mock, randint_mock):
        #dealer hand==21, user hand==21
        output_6 = run_test([7, 7, 7], ['y','n'], [7, 7, 7], randint_mock, input_mock)
        expected_result_6 = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 7\n" \
                   "Drew a 7\n" \
                   "You have 14. Hit (y/n)? y\n" \
                   "Drew a 7\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!"\
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 7\n" \
                   "Drew a 7\n" \
                   "Dealer has 14.\n" \
                   "Drew a 7\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!"\
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Push\n"
        self.assertEqual(output_6, expected_result_6)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_win_case_1(self, input_mock, randint_mock):
        #user hand ==21, dealer hand>21
        output_7 = run_test([7, 7, 7], ['y', 'n'], [3, 5, 10], randint_mock, input_mock)
        expected_result_7 = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 7\n" \
                   "Drew a 7\n" \
                   "You have 14. Hit (y/n)? y\n" \
                   "Drew a 7\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 9\n" \
                   "Dealer has 12.\n" \
                   "Drew a 10\n" \
                   "Final hand: 22.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"
        self.assertEqual(output_7, expected_result_7)


    # Write all your tests above this. Do not delete this line.

if __name__ == '__main__':
    main()

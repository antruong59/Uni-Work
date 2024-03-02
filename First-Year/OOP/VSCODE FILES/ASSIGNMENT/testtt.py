'''
    Test file for testing function in WoM_truan004.py (using unittest)
'''

import unittest 
import WoM_truan004

class TestFunction(unittest.TestCase):

    '''Test getUserCommand function in class Game'''
    def test_getUserCommand(self):
        check = WoM_truan004.Game()
        test = check.getUserCommand('\nWhat would you like to do?\n (r) register a new user\n (s) show the score board\n (p) play a game\n (q) quit\n> ')
        self.assertIsInstance(test, bool)

    '''Test register function in class Game'''
    def test_register(self):
        check = WoM_truan004.Game()
        test = check.register()
        self.assertIsInstance(test, list)

    '''Test validateInput function in class Game'''
    def test_validateInput(self):
        check = WoM_truan004.Game()
        test = check.validateInput('How many players (2-4)?\n> ', 2, 5, 'The number of players must be in range (2-4)! Please re-enter.')
        self.assertIsInstance(test, int)

    '''Test check function in class FeedBack'''
    def test_checkFeedback(self):
        check = WoM_truan004.FeedBack
        test = check.check('An', {'An':'RGBY'}, 'RGBY')
        self.assertEqual(test, 'K K K K ')

    '''Test getCode function in class Player'''
    def test_getCode(self):
        check = WoM_truan004.Player(2, 5, ['R', 'G', 'B', 'Y', 'W', 'K'], ['An', 'VIKI'],  [WoM_truan004.Human('An'), WoM_truan004.Computer('VIKI')])
        test = check.getCode('An')
        self.assertIsInstance(test, str)

    '''Test setCode function in class Player'''
    def test_setCode(self):
        check = WoM_truan004.Player(2, 5, ['R', 'G', 'B', 'Y', 'W', 'K'], ['An', 'VIKI'],  [WoM_truan004.Human('An'), WoM_truan004.Computer('VIKI')])
        test = check.setCode()
        self.assertIsInstance(test, dict)

    '''Test getAverage function in class Human'''
    def test_getAverage(self):
        check = WoM_truan004.Human('An')
        check.score = 10
        check.listScore = [0, 4, 3, 2, 1]
        test = check.getAverage()
        self.assertEqual(test, 2.50)

    '''Test getName function in class Human'''
    def test_getName(self):
        check = WoM_truan004.Human('An')
        test = check.getName()
        self.assertEqual(test, 'An')

    '''Test computerSet function in class Computer'''
    def test_computerSet(self):
        check = WoM_truan004.Computer
        test = check.computerSet()
        self.assertIsInstance(test, str)

unittest.main()
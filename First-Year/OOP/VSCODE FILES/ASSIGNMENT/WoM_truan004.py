#
# File: WoM_truan004.py
# Descrition: This is a module Game World of Mastermind. This Game allows players to take turn to set code and break code, either among Human players or Computer Players (2 - 4 players/ game)
# Author: An Ngoc Truong
# Student ID: 110313636
# Email ID: truan004
# This is my own work as defined by
# the University's Academic Misconduct Policy.
#

'''ASSIGNMENT 2 - OOP - WORLD OF MASTERMIND'''

'''Import library (Abstract and Random)'''
from abc import ABC, abstractmethod
import random


'''
    Define World of Mastermind class
    Use run() function to activate the whole program
'''
class WorldOfMastermind:
    def run(self):
        print('Welcome to the World of Mastermind!\nDeveloped by An Ngoc Truong\nCOMP 1046 Object-Oriented Programming\n')

        '''Check whether in game or not, using inGame variable --> bool'''
        inGame = True
        while inGame == True:

            '''Start the game with command menu'''
            inGame = Game().getUserCommand(Game.menu)


'''
    Define interface MainMenuGame as asbtract class 
    --> the template for the Game class 
'''
class MainMenuGame(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def getUserCommand(self):
        pass

    @abstractmethod
    def register(self):
        pass

    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def showScoreBoard(self):
        pass


'''
    Define Exception classes inherited from Python Built-in class Exception
    Create specified exceptions for this program
'''
class BlankName(Exception):
    '''Not allow blank name'''
    pass


class NameAlreadyExist(Exception):
    '''Name has already existed'''
    pass


class InvalidCommand(Exception):
    '''Command is not valid'''
    pass


class NotInRange(Exception):
    '''Number is out of range'''
    pass


'''
    Define Game class which implements the MainMenuGame class
    It overrides and extend the MainMenuGame class, use abstract class as a template
'''
class Game(MainMenuGame):

    '''Assign class variables'''

    __validCommand = ['r', 's', 'p', 'q'] 

    menu = '\nWhat would you like to do?\n (r) register a new user\n (s) show the score board\n (p) play a game\n (q) quit\n> '

    '''Store register name'''
    listRegister = [] 

    validColor = ['R', 'G', 'B', 'Y', 'W', 'K']

    '''Store list of object create in Register'''
    listObject = []

    def __init__(self):
        super().__init__()


    '''Define function to get user command'''
    def getUserCommand(self, displayCommand):

        '''Validate user input for main menu'''
        try:
            userCommand = input(displayCommand)
            if userCommand not in self.__validCommand:
                raise InvalidCommand
            elif userCommand == 'r':
                self.register()
            elif userCommand == 's':
                self.showScoreBoard()
            elif userCommand == 'p':
                self.play()
            else:
                print('Thank you for playing the World of Mastermind!')
                return False

        except InvalidCommand:
            print('Invalid command! Please re-enter the command either r, s, p or q')

        finally:

            '''End of the game'''
            if userCommand != 'q':
                return True


    '''Define function that allows user to register in program'''
    def register(self):

        '''Validate legal name of user'''
        try:
            rName = input('What is the name of the new user?\n> ')
            if ''.join(rName.split()) == '':
                raise BlankName
            elif rName in self.listRegister or rName in Computer.computer:
                raise NameAlreadyExist

        except BlankName:
            print('Name can not be blank.')

        except NameAlreadyExist:
            print('Sorry, the name is already taken.')

        else:

            '''Get rid of spaces in name'''
            registerName = rName.strip()

            '''Add the new registered user''' 
            self.listRegister.append(registerName)

            '''Create an object for that user, then add to list of objects'''
            self.listObject.append(Human(registerName))

            print(f'Welcome, {registerName}!')

        return self.listRegister


    '''Define function to validate input with number'''
    def validateInput(self, command, min, max, message):
        invalid = True
        while invalid == True:
            try:
                userInput = input(command)

                if userInput.isdigit() == False:
                    raise TypeError
                elif int(userInput) not in range(min, max):
                    raise NotInRange
                else:
                    invalid = False

            except TypeError:
                print('You must enter a number.')

            except NotInRange:

                '''Raise appropriate message specify for that error'''
                print(message)

        return int(userInput)


    '''
        Define function that allow user to play the game
        Most of the game logic occurs here
    '''
    def play(self):

        '''Store list of players in a game'''
        pList = []

        '''Store list of objects in a game'''
        playListObject = []

        print('Let\'s play the game of Mastermind!')

        '''Get the number of players in game using validateInput function'''
        noPlayer = self.validateInput('How many players (2-4)?\n> ', 2, 5, 'The number of players must be in range (2-4)! Please re-enter.')

        '''Get the name of the players in game'''
        for i in range(1, noPlayer + 1):
            pName = input(f'What is the name of player #{i}?\n> ')

            '''Validate user input for name'''
            while (pName not in self.listRegister and pName not in Computer.computer) or pName in pList:
                if pName not in self.listRegister and pName not in Computer.computer:
                    print('Invalid user name.')
                    pName = input(f'What is the name of player #{i}?\n> ')

                elif pName in pList:
                    print(f'{pName} is already in the game.')
                    pName = input(f'What is the name of player #{i}?\n> ')

            '''Add name to list of players in game'''
            pList.append(pName)

            '''Create a copy of listObject in Game, order by position in a game turn'''
            if pName in Computer.computer:

                '''Create and add Computer object in game'''
                playListObject.append(Computer(pName))
                
            else:

                '''Add existed Human object in game'''
                for j in range(0, len(self.listObject)):
                    name = self.listObject[j]
                    
                    '''Check for object in list of object that already registed'''
                    if pName == name.getName():
                        playListObject.append(self.listObject[j])
                        
                    else:
                        continue
        
        '''Get the number of attempts in game using validateInput function'''
        noAttempts = self.validateInput('How many attempts will be allowed for each player (5-10)?\n> ',5, 11, 'The number of attemps must be in range (5-10)! Please re-enter.')

        '''Create new object Player that allows players to do function in game'''
        new = Player(noPlayer, noAttempts, self.validColor, pList, playListObject)

        '''
            Players set code
            Call out the setCode function of object Player
        '''
        playerBreakCode = new.setCode()

        # print('Debug: ', playerBreakCode)
        
        '''
            Players make guesses
            Call out the setCode function of object Player
        '''
        guess = new.makeGuess()
        
        # Debug: return guess


    '''
        Define function that show score board to user
        Record users' game history
    '''
    def showScoreBoard(self):

        '''Required register first before displaying score board'''
        if len(self.listRegister) == 0:
            print('There is no player to display in score board!\nPlease register first!')

        else:

            '''Display score board'''
            print('=====================================')
            print(format('Name', '<16s'), format('Score', '<5s'), format('Games', '<5s'), format('Average', '<8s'))
            print('=====================================')
            for i in self.listObject:
                print(format(f'{i.getName()}', '<16s'), format(f'{sum(i.listScore)}', '<5s'), format(f'{len(i.listScore) - 1}', '<5s'), format(f'{i.getAverage()}', '<8s'))
            print('=====================================')


'''
    Define class that give feedback for each guess of players
'''
class FeedBack:
    __keyPegs = ['K ', 'W ']

    def check(key, playerBreakCode, makeGuess):
        countK = 0
        countW = 0

        '''Validate each character in guess code whether it is correct and in the right position'''
        for i in range(0, len(playerBreakCode[key])):

            '''If the character is both correct and in the right position'''
            if makeGuess[i] == playerBreakCode[key][i]:
                countK += 1

                '''If the character is correct'''
            elif makeGuess[i] in list(playerBreakCode[key]) and makeGuess.count(makeGuess[i]) == playerBreakCode[key].count(makeGuess[i]):
                countW += 1

        '''Give feedback to code'''
        result = countK * FeedBack.__keyPegs[0] + countW * FeedBack.__keyPegs[1]

        '''If user got all wrong --> feedback = 0'''
        if result == '':
            result = 0

        return result


'''
    Define Player class with Player's set code and make guess functions
'''
class Player:

    '''Initialise the instances/attributes of Player'''
    def __init__(self, noPlayer, noAttempts, validColor, pList, listObject):
        self.__noPlayer = noPlayer
        self.__noAttempts = noAttempts
        self.__validColor = validColor
        self.__pList = pList
        self.__listObject = listObject

        '''Dictionary stores the sequence of "name : setCode" pairs'''
        self.__playerBreakCode = {}

        '''Dictionary stores the sequence of "name : attempts to break code" pairs'''
        self.__listAttempts = {}

        '''Dictionary stores the sequence of "name : score" pairs'''
        self.listScore = {}
        

    '''Define function that check and return valid code'''
    def getCode(self, name):

        '''Call the computer make code function'''
        if name in Computer.computer:
            code = Computer.computerSet()
            print('Debug: ', code)

        else:
            '''Validate the input code from players'''
            inValidateColor = True
            while inValidateColor == True:
                try:
                    code = input('Please enter the code:\n> ')

                    '''Check for the length of the code (must be 4 characters)'''
                    if len(code) != 4:
                        raise InvalidCommand

                    '''Check for characters (must be in valid code)'''
                    for char in list(code):
                        if char not in self.__validColor:
                            raise InvalidCommand
                    else:
                        inValidateColor = False

                except InvalidCommand:
                    print('Invalid code.\nIt must be exactly four characters, each can be R, G, B, Y, W, or K.')

        return code


    '''Define function that allows players to set code in game'''
    def setCode(self):

        '''Players take turn to set code in game'''
        for i in range(0, self.__noPlayer):
            if i == self.__noPlayer - 1:
                print(
                    f'* {self.__pList[i]}\'s turn to set the code for {self.__pList[0]} to break.')
            else:
                print(
                    f'* {self.__pList[i]}\'s turn to set the code for {self.__pList[i + 1]} to break.')

            '''Set code using getCode function'''
            setCode = self.getCode(self.__pList[i])

            '''Add "name : set code" pairs in dictionary self.__playerBreakCode'''
            if i == int(self.__noPlayer) - 1:
                self.__playerBreakCode[self.__pList[0]] = setCode
                print(f'The code is now set for {self.__pList[0]} to break.')
            else:
                self.__playerBreakCode[self.__pList[i + 1]] = setCode
                print(f'The code is now set for {self.__pList[i + 1]} to break.')

        return self.__playerBreakCode


    '''Define function that allows players to set code in game'''
    def makeGuess(self):

        '''Loop through players on first attempt'''
        for i in range(0, self.__noPlayer):

            '''Reset player object's guess list'''
            self.__listObject[i].guess = []

            '''Reset player object's attempts counter'''
            self.__listObject[i].attempts = 0
            
            print(f'* {self.__pList[i]}\'s turn to guess the code.')
            print(f'Previous attempts: 0')
            print(f'Attempts left: {self.__noAttempts}')

            '''Make guess using getCode function'''
            makeGuess = self.getCode(self.__pList[i])

            '''Give feedback to player's guesses'''
            check = FeedBack.check(self.__pList[i], self.__playerBreakCode, makeGuess)
            print(f'{self.__pList[i]}\'s guess: {makeGuess}')
            print(f'Feedback: {check}')

            '''Add pair [makeGuess, check] into player's guess list'''
            self.__listObject[i].guess.append([makeGuess, check])

            attempts = self.__listObject[i].attempts
            attempts += 1
            
            '''Modify score for human player only'''
            if self.__pList[i] not in Computer.computer:
                self.__listObject[i].score = self.__noAttempts - 1

            '''Player broke code'''
            if check == 'K K K K ':
                print(f'{self.__pList[i]} broke the code in 1 attempt!')

                '''Add players' score into list of score'''
                self.listScore[self.__pList[i]] = self.__listObject[i].score
                continue
        
        '''Loop for the rest attempts'''
        j = 1
        while 0 < j < self.__noAttempts:

            '''Loop through players'''
            for i in range(0, self.__noPlayer):

                '''Player broke code'''
                if self.__listObject[i].guess[-1][1] == 'K K K K ': 

                    '''Add players' attempts into list of attempts'''
                    self.__listAttempts[self.__pList[i]] = self.__listObject[i].attempts + 1
                    continue
                
                else:
                    print(f'* {self.__pList[i]}\'s turn to guess the code.')
                    print(f'Previous attempts: {j}')
                    print('==============')
                    print('Code Feedback')
                    print('==============')

                    # '''Display players' previous guesses'''
                    for k in range(0, j):
                        print(f'{self.__listObject[i].guess[k][0]} {self.__listObject[i].guess[k][1]}')

                    #print('Debug: Guess list ', self.__listObject[i].guess)

                    print('==============')
                    print(f'Attempts left: {self.__noAttempts - j}')

                    '''Make guess using getCode function'''
                    makeGuess = self.getCode(self.__pList[i])

                    '''Give feedback to player's guesses'''
                    check = FeedBack.check(self.__pList[i], self.__playerBreakCode, makeGuess)
                    print(f'{self.__pList[i]}\'s guess: {makeGuess}')
                    print(f'Feedback: {check}')

                    '''Add pair [makeGuess, check] into player's guess list'''
                    self.__listObject[i].guess.append([makeGuess, check])

                    '''Modify players' attempts'''
                    self.__listObject[i].attempts += 1
            
                    '''Modify score for human player only'''
                    if self.__pList[i] not in Computer.computer:
                        self.__listObject[i].score -= 1

                    '''Player broke code'''
                    if check == 'K K K K ':
                        print(f'{self.__pList[i]} broke the code in {j + 1} attempts!')

                        '''Add players' score into list of score'''
                        self.listScore[self.__pList[i]] = self.__listObject[i].score
                
                '''Last attempt'''        
                if j == self.__noAttempts - 1:

                    '''Add players' attempts into list of attempts'''
                    self.__listAttempts[self.__pList[i]] = self.__listObject[i].attempts + 1
                    if self.__pList[i] not in Computer.computer:
                        '''Add players' score into list of score'''
                        self.listScore[self.__pList[i]] = self.__listObject[i].score
                    
                    print(f'{self.__pList[i]} failed to break the code.')
                    
                if i == self.__noPlayer -1 and j == self.__noAttempts - 1:
                    j += 1
                    
            j += 1

        print('\nThe game is now finished.')

        '''
            Calculate human players' score:

            Score = player_i's attempts left + player_i+1's attempts to break the code
            *Notes: player_i+1 is the player who player_i set code for
        
        '''
        for i in range(0, len(self.__pList)):
            if self.__pList[i] not in Computer.computer:

                '''Player at the last of the list'''
                if i == len(self.__pList) - 1:

                    '''Caculate player_i attempt left'''
                    attemptLeft = self.listScore[self.__pList[i]]

                    '''Calculate player_i+1 attempt'''
                    othersAttempt = self.__listAttempts[self.__pList[0]]

                    '''Calculate score'''
                    self.listScore[self.__pList[i]] += self.__listAttempts[self.__pList[0]]
                    self.__listObject[i].score = self.listScore[self.__pList[i]]

                    '''Add score into list of score'''
                    self.__listObject[i].listScore.append(self.__listObject[i].score)
                    print(f'{self.__pList[i]} receives {attemptLeft} + {othersAttempt} = {self.__listObject[i].score} points.')
                else:

                    '''Caculate player_i attempt left'''
                    attemptLeft = self.listScore[self.__pList[i]]

                    '''Calculate player_i+1 attempt'''
                    othersAttempt = self.__listAttempts[self.__pList[i + 1]]

                    '''Calculate score'''
                    self.listScore[self.__pList[i]] += self.__listAttempts[self.__pList[i + 1]]
                    self.__listObject[i].score = self.listScore[self.__pList[i]]

                    '''Add score into list of score'''
                    self.__listObject[i].listScore.append(self.__listObject[i].score)
                    print(f'{self.__pList[i]} receives {attemptLeft} + {othersAttempt} = {self.__listObject[i].score} points.')

            else:

                '''If player is Computer'''
                continue

        return self.listScore


'''
    Define Human class which is inherited from Player class
    Inherit and extend Player class
'''
class Human(Player):

    '''Initialise Human object with name of player is required'''
    def __init__(self, playerName):
        self.__playerName = playerName
        self.score = 0
        self.attempts = 0

        '''List history of human guess and feedback'''
        self.guess = []

        '''List of human score (default 0 at first score)'''
        self.listScore = [self.score]

        '''Average of human score'''
        self.average = 0

    '''Calculate average score of all games'''
    def getAverage(self):

        '''Avoid DevideByZero Error'''
        try:
            self.average = sum(self.listScore) / (len(self.listScore) - 1)
        except Exception:
            self.average = 0

        return self.average


    def __repr__(self):
        return self.__playerName


    '''
        Get name of human player (as name is private variable pf Human class)
        --> Can be viewed but not modified outside the class 
    '''
    def getName(self):
        return self.__playerName


'''
    Define Computer class which is inherited from Player class
    Inherit and extend Player class
'''
class Computer(Player):

    '''Valid name of computer'''
    computer = ['HAL9000', 'VIKI']

    '''Initialise Computer object with name of player is required'''
    def __init__(self, cname):
        self.__playerName = cname
        self.attempts = 0

        '''List history of computer guess and feedback'''
        self.guess = []

    def __repr__(self):
        return self.__playerName + ' computer player'

    '''Automatically generate code by computer (use random)'''
    def computerSet():
        setCode = ''

        '''Choose random 4 characters, each in valid color'''
        listRandom = random.choices(Game.validColor, weights=[4, 4, 4, 4, 4, 4], k=4)

        for i in listRandom:
            setCode += i

        return setCode


'''Activate the program by call World of Mastermind object and its run function'''
x = WorldOfMastermind()
x.run()





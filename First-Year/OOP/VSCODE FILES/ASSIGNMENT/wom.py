'''
    This is a draft of final assignment with debugging printed elements to keep track of the process of the game
'''



from abc import ABC, abstractmethod
import random


class WorldOfMastermind:
    def run(self):
        print('Welcome to the World of Mastermind!\nDeveloped by An Ngoc Truong\nCOMP 1046 Object-Oriented Programming\n')
        inGame = True
        while inGame == True:
            inGame = Game().getUserCommand(Game.menu)


class MainMenuGame(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def getUserCommand(self):
        pass


class BlankName(Exception):
    pass


class NameAlreadyExist(Exception):
    pass


class InvalidCommand(Exception):
    pass


class NotInRange(Exception):
    pass


class Game(MainMenuGame):
    __validCommand = ['r', 's', 'p', 'q']
    menu = '\nWhat would you like to do?\n (r) register a new user\n (s) show the score board\n (p) play a game\n (q) quit\n> '
    listRegister = []
    validColor = ['R', 'G', 'B', 'Y', 'W', 'K']
    listObject = []

    def __init__(self):
        super().__init__()
        # self.


    def getUserCommand(self, displayCommand):
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
                print('Thanks for playing!')
                return False

        except InvalidCommand:
            print('Invalid command! Please re-enter the command either r, s, p or q')

        finally:
            if userCommand != 'q':
                return True

    def register(self):
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
            registerName = rName.strip()
            self.listRegister.append(registerName)
            self.listObject.append(Human(registerName))
            print(self.listObject)
            print(f'Welcome, {registerName}!')

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
                print(message)

        return int(userInput)

    def play(self):
        pList = []
        playListObject = []
        print('Let\'s play the game of Mastermind!')

        noPlayer = self.validateInput('How many players (2-4)?\n> ', 2, 5, 'The number of players must be in range (2-4)! Please re-enter.')

        for i in range(1, noPlayer + 1):
            pName = input(f'What is the name of player #{i}?\n> ')
            while (pName not in self.listRegister and pName not in Computer.computer) or pName in pList:
                if pName not in self.listRegister and pName not in Computer.computer:
                    print('Invalid user name.')
                    pName = input(f'What is the name of player #{i}?\n> ')

                elif pName in pList:
                    print(f'{pName} is already in the game.')
                    pName = input(f'What is the name of player #{i}?\n> ')

            print('Add Name')
            pList.append(pName)
            if pName in Computer.computer:
                playListObject.append(Computer(pName))
                print(playListObject)
                # Computer(pName).guess = []
                # print(Computer(pName).guess)

            else:
                for j in range(0, len(self.listObject)):
                    name = self.listObject[j]
                    print(type(name))
                    if pName == name.getName():
                        playListObject.append(self.listObject[j])
                        print(name)
                    else:
                        continue
                # Human(pName).guess = []
                # print(Human(pName).guess)
            print('New list object', playListObject)
            print(self.listObject)
            print(pList)

        noAttempts = self.validateInput('How many attempts will be allowed for each player (5-10)?\n> ',5, 11, 'The number of attemps must be in range (5-10)! Please re-enter.')

        new = Player(noPlayer, noAttempts, self.validColor, pList, playListObject)
        playerBreakCode = new.setCode()
        print(playerBreakCode)
        
        guess = new.makeGuess()
        
        print(guess)
        

        return guess


        

    def showScoreBoard(self):
        print('=====================================')
        print(format('Name', '<16s'), format('Score', '<5s'), format('Games', '<5s'), format('Average', '<8s'))
        print('=====================================')
        for i in self.listObject:
            print(format(f'{i.getName()}', '<16s'), format(f'{sum(i.listScore)}', '<5s'), format(f'{len(i.listScore) - 1}', '<5s'), format(f'{i.getAverage()}', '<8s'))
        print('=====================================')
        for i in self.listObject:
            print(i.getName(), i.listScore)


class FeedBack:
    __keyPegs = ['K ', 'W ']

    def check(key, playerBreakCode, makeGuess):
        countK = 0
        countW = 0
        for i in range(0, len(playerBreakCode[key])):
            if makeGuess[i] == playerBreakCode[key][i]:
                countK += 1
            elif makeGuess[i] in list(playerBreakCode[key]) and makeGuess.count(makeGuess[i]) == playerBreakCode[key].count(makeGuess[i]):
                countW += 1
            print(i)

        result = countK * FeedBack.__keyPegs[0] + countW * FeedBack.__keyPegs[1]
        if result == '':
            result = 0
        return result


class Player:
    def __init__(self, noPlayer, noAttempts, validColor, pList, listObject):
        self.__noPlayer = noPlayer
        self.__noAttempts = noAttempts
        self.__validColor = validColor
        self.__pList = pList
        self.__listObject = listObject
        self.__playerBreakCode = {}
        self.__listAttempts = {}
        self.listScore = {}
        

    def getCode(self, name):
        if name in Computer.computer:
            code = Computer.computerSet()
            print(code)

        else:
            inValidateColor = True
            while inValidateColor == True:
                try:
                    code = input('Please enter the code:\n> ')
                    print(list(code))
                    if len(code) != 4:
                        raise InvalidCommand
                    for char in list(code):
                        if char not in self.__validColor:
                            raise InvalidCommand
                    else:
                        inValidateColor = False

                except InvalidCommand:
                    print(
                        'Invalid code.\nIt must be exactly four characters, each can be R, G, B, Y, W, or K.')

        return code

    def setCode(self):
        for i in range(0, self.__noPlayer):
            if i == self.__noPlayer - 1:
                print(
                    f'* {self.__pList[i]}\'s turn to set the code for {self.__pList[0]} to break.')
            else:
                print(
                    f'* {self.__pList[i]}\'s turn to set the code for {self.__pList[i + 1]} to break.')

            setCode = self.getCode(self.__pList[i])

            if i == int(self.__noPlayer) - 1:
                self.__playerBreakCode[self.__pList[0]] = setCode
                print(f'The code is now set for {self.__pList[0]} to break.')
            else:
                self.__playerBreakCode[self.__pList[i + 1]] = setCode
                print(f'The code is now set for {self.__pList[i + 1]} to break.')

        return self.__playerBreakCode, self.__noAttempts

    def makeGuess(self):
        # for i in range(len(self.__pList)):
        #     if self.__pList[i] in Computer.computer:
        #         obj = Computer(self.__pList[i])
        #         print(obj)
        #         self.__listObject.insert(i, obj)
        #         print(self.__listObject)
        #     else:
        #         continue

        for i in range(0, self.__noPlayer):
            # print(self.listObject)
            # print(self.listObject[i].playerName)
            self.__listObject[i].guess = []
            self.__listObject[i].attempts = 0
            print(self.__listObject[i].guess)

            print(f'* {self.__pList[i]}\'s turn to guess the code.')
            print(f'Previous attempts: 0')
            print(f'Attempts left: {self.__noAttempts}')

            makeGuess = self.getCode(self.__pList[i])
            check = FeedBack.check(self.__pList[i], self.__playerBreakCode, makeGuess)
            print(f'{self.__pList[i]}\'s guess: {makeGuess}')
            print(f'Feedback: {check}')

            self.__listObject[i].guess.append([makeGuess, check])

            attempts = self.__listObject[i].attempts
            print('attempts before add', attempts)
            attempts += 1
            
            print('attempts', attempts)
            if self.__pList[i] not in Computer.computer:
                self.__listObject[i].score = self.__noAttempts - 1
                attemptLeft = self.__listObject[i].score
                print('attempts left', attemptLeft)

            

            # print(self.listObject[i].playerName, self.listObject[i].guess)

            if check == 'K K K K ':
                print(f'{self.__pList[i]} broke the code in 1 attempt!')
                self.listScore[self.__pList[i]] = self.__listObject[i].score
                print('SCORE ', self.listScore)
                continue

        j = 1
        while 0 < j < self.__noAttempts:
            for i in range(0, self.__noPlayer):
                # if self.__pList[i] == 'Passed':
                #     continue

                if self.__listObject[i].guess[-1][1] == 'K K K K ': #or self.listObject[i].guess[0][1] == 'K K K K ':
                    print('Working in here!!!')
                    self.__listAttempts[self.__pList[i]] = self.__listObject[i].attempts + 1
                    print('list attempts ', self.__listAttempts)
                    continue
                
                else:
                    print(f'* {self.__pList[i]}\'s turn to guess the code.')
                    print(f'Previous attempts: {j}')
                    print('==============')
                    print('Code Feedback')
                    print('==============')
                    for k in range(0, j):
                        print(f'{self.__listObject[i].guess[k][0]} {self.__listObject[i].guess[k][1]}')
                    print('Guess list ', self.__listObject[i].guess)
                    print('==============')
                    print(f'Attempts left: {self.__noAttempts - j}')

                    makeGuess = self.getCode(self.__pList[i])
                    check = FeedBack.check(self.__pList[i], self.__playerBreakCode, makeGuess)
                    print(f'{self.__pList[i]}\'s guess: {makeGuess}')
                    print(f'Feedback: {check}')

                    self.__listObject[i].guess.append([makeGuess, check])

                    # print(self.listObject[i].playerName, self.listObject[i].guess)
                    self.__listObject[i].attempts += 1
            
                    print('attempts', self.__listObject[i].attempts)
                    if self.__pList[i] not in Computer.computer:
                        self.__listObject[i].score -= 1
                        attemptLeft = self.__listObject[i].score
                        print('attempts left', attemptLeft)
                        

                    if check == 'K K K K ':
                        print(f'{self.__pList[i]} broke the code in {j + 1} attempts!')
                        print('attempts left', self.__listObject[i].score)
                        self.listScore[self.__pList[i]] = self.__listObject[i].score
                        print('SCORE ', self.listScore)
                        #self.__pList[i] = 'Passed'
                        
                        print(self.__pList)
                        print(self.__listObject)
                    
                if j == self.__noAttempts - 1:
                    self.__listAttempts[self.__pList[i]] = self.__listObject[i].attempts + 1
                    print('list attempts ', self.__listAttempts)
                    if self.__pList[i] not in Computer.computer:
                        self.listScore[self.__pList[i]] = self.__listObject[i].score
                        print('SCORE ', self.listScore)

                    print(f'{self.__pList[i]} failed to break the code.')
                    
                if i == self.__noPlayer - 1 and j == self.__noAttempts - 1: 
                    j += 1
                    
            j += 1

        print('\nThe game is now finished.')

        for i in range(0, len(self.__pList)):
            if self.__pList[i] not in Computer.computer:
                if i == len(self.__pList) - 1:
                    attemptLeft = self.listScore[self.__pList[i]]
                    othersAttempt = self.__listAttempts[self.__pList[0]]
                    self.listScore[self.__pList[i]] += self.__listAttempts[self.__pList[0]]
                    self.__listObject[i].score = self.listScore[self.__pList[i]]
                    self.__listObject[i].listScore.append(self.__listObject[i].score)
                    print(f'{self.__pList[i]} receives {attemptLeft} + {othersAttempt} = {self.__listObject[i].score} points.')
                else:
                    attemptLeft = self.listScore[self.__pList[i]]
                    othersAttempt = self.__listAttempts[self.__pList[i + 1]]
                    self.listScore[self.__pList[i]] += self.__listAttempts[self.__pList[i + 1]]
                    self.__listObject[i].score = self.listScore[self.__pList[i]]
                    self.__listObject[i].listScore.append(self.__listObject[i].score)
                    print(f'{self.__pList[i]} receives {attemptLeft} + {othersAttempt} = {self.__listObject[i].score} points.')

            else:
                continue
            print('list score ', self.listScore)
        return self.listScore


class Human(Player):
    def __init__(self, playerName):
        self.__playerName = playerName
        self.score = 0
        self.attempts = 0
        self.guess = []
        self.listScore = [self.score]
        self.average = 0

    def getAverage(self):
        try:
            self.average = sum(self.listScore) / (len(self.listScore) - 1)
        except Exception:
            self.average = 0

        return self.average


    def __repr__(self):
        return self.__playerName

    def getName(self):
        return self.__playerName

    # def getAverage(self):
    #     self.average = sum(self.listScore) / len(self.listScore)

    #     return self.


class Computer(Player):
    computer = ['HAL9000', 'VIKI']

    def __init__(self, cname):
        self.__playerName = cname
        self.attempts = 0
        self.guess = []

    def __repr__(self):
        return self.__playerName + ' computer player'

    def computerSet():
        setCode = ''
        listRandom = random.choices(Game.validColor, weights=[4, 4, 4, 4, 4, 4], k=4)
        for i in listRandom:
            setCode += i
        return setCode


x = WorldOfMastermind()
x.run()

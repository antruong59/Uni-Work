class SoccerTeam:
    def __init__(self, name):
        self.__name = name
        self.__won = 0
        self.__draws = 0
        self.__lost = 0
        self.__score = 0
        self.__goalFor = 0
        self.__goalAgainst = 0

    def add_result(self, goalFor, goalAgainst):
        self.__goalFor += goalFor
        self.__goalAgainst += goalAgainst

        if goalFor > goalAgainst:
            self.__won += 1
            self.__score += 3

        elif goalFor < goalAgainst:
            self.__lost += 1
        
        else:
            self.__draws += 1
            self.__score += 1

    def score(self):
        return self.__score

    def goalDifference(self):
        return self.__goalFor - self.__goalAgainst

    def print_report(self):
        print(f'{self.__name} W:{self.__won} D:{self.__draws} L:{self.__lost} GF:{self.__goalFor} GA:{self.__goalAgainst} GD:{self.goalDifference()} Pts:{self.__score}')

stMatildas = SoccerTeam('Matildas')
stMatildas.print_report()
stMatildas.add_result(2, 1)
stMatildas.add_result(2, 4)
stMatildas.add_result(0, 0)
stMatildas.print_report()

class Group:
    def __init__(self, name):
        self.__name = name
        self.__teams = []

    def add_team(self, name):
        self.__teams.append(name)

    def add_result(self, team1, team2, goal1, goal2):
        team1.add_result(goal1, goal2)
        team2.add_result(goal2, goal1)

    def print_table(self):
        self.__teams.sort(key=lambda t: (t.score(), t.goalDifference()), reverse=True)
        for name in self.__teams:
            name.print_report()

matildas = SoccerTeam('M')
sweden = SoccerTeam('S')
usa = SoccerTeam('U')

group = Group('G')
group.add_team(matildas)
group.add_team(sweden)
group.add_team(usa)
group.add_result(sweden, usa, 5, 4)
group.add_result(matildas, usa, 0, 1)
group.add_result(sweden, matildas, 3, 2)

group.print_table()


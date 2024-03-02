
class ScoreTracker():
    def __init__(self, score_track):
        self.score_track = score_track
        self.__scoreList = [self.score_track]

    def add_score(self,addScore):
        self.addScore = addScore
        self.__scoreList.append(self.addScore)

    def min_score(self):
        return min(self.__scoreList)

    def max_score(self):
        return max(self.__scoreList)

    def number_of_scores(self):
        return len(self.__scoreList)

    def print_scores(self):
        print(self.__scoreList)


class Game():
    def __init__(self, name, age, score):
        self.player_name = name
        self.age = age
        self.__score = score
        self.scores = ScoreTracker(score_track = self.__score)

    def current_score(self):
        return self.__score

    def report_info(self):
        print('Player name:', self.player_name, '/ Age:', self.age, '/ Score:', self.__score)
        self.scores.print_scores()

    def add_win(self):
        self.__score += 1
        self.scores.add_score(self.__score)
    
    def deduct_loss(self):
        if self.__score != 0:
            self.__score -= 1
        self.scores.add_score(self.__score)

# task 1

print('Task 1')
new_game = Game('Smith', 31, 0 )
new_game.report_info()
new_game.add_win()
new_game.add_win()
new_game.report_info()
print('Current Score:' + str(new_game.current_score()))
new_game.deduct_loss()
print('Current Score:' + str(new_game.current_score()))

print('\n')

# task 2

print('Task 2')
new_tracker=ScoreTracker(50)
new_tracker.add_score(60)
new_tracker.add_score(70)
print('Minimum score:' + str(new_tracker.min_score()))
print('Maximum score:' + str(new_tracker.max_score()))
print('Number of scores:' + str(new_tracker.number_of_scores()))
new_tracker.print_scores()
print('\n')

# task 3

print('Task 3')
new_game = Game('Berkley', 30, 50)
new_game.add_win()
new_game.deduct_loss()
new_game.deduct_loss()
new_game.report_info()
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

import random
moves = ['rock', 'paper', 'scissors']
Tie = [0, 0]
Player1 = [1, 0]
Player2 = [0, 1]
numberOfRounds = 9

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):
        # return super().move() =>
        # We need to override the whole move() method to the RANDOM approach
        return moves[random.randint(0, 2)]


# IN THOSE BOTH CLASSES, FOR THE FIRST ROUND =>
# I HAVE IMPLEMENTED THE RANDOM APPROCH
class ReflectPlayer(Player):
    def __init__(self):
        self.nextMove = ""

    def move(self):
        if self.nextMove == "":
            return moves[random.randint(0, 2)]
        return self.nextMove

    def learn(self, my_move, their_move):
        self.nextMove = their_move


class CyclePlayer(Player):
    def __init__(self):
        self.nextMove = ""

    def move(self):
        if self.nextMove == "":
            return moves[random.randint(0, 2)]
        return self.nextMove

    def learn(self, my_move, their_move):
        self.nextMove = moves[(moves.index(my_move) + 1) % 3]


class HumanPlayer(Player):
    def move(self):
        # return super().move() =>
        # We need to override the whole move() method to USER INPUT approach
        while True:
            userChoice = input("Rock, paper, scissors? > ")
            if userChoice.lower() in moves:
                return userChoice.lower()


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


def roundStatus(move1, move2):
    print(f"You played {move1}.")
    print(f"Opponent played {move2}.")
    if move1 == move2:
        print("\u001b[34m** TIE **\u001b[0m")
        return Tie
    if beats(move1, move2):
        print("\u001b[32m** PLAYER ONE WINS **\u001b[0m")
        return Player1
    else:
        print("\u001b[31m** PLAYER TWO WINS **\u001b[0m")
        return Player2


def gameStatus(totalScore):
    print("------------------")
    print(f"Score: Player One {totalScore[0]}, " +
          f"Player Two {totalScore[1]}")
    if totalScore[0] < totalScore[1]:
        print("\u001b[31m** PLAYER TWO WON! **\u001b[0m")
        print("Game over!")
    elif totalScore[0] > totalScore[1]:
        print("\u001b[32m** PLAYER ONE WON **\u001b[0m")
        print("\u001b[32m** CONGRATULATIONS! **\u001b[0m")
    else:
        print("\u001b[34m** TIE **\u001b[0m")
        print("Game over!")


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.totalScore = [0, 0]

    def getScore(self):
        return self.totalScore

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        roundScore = roundStatus(move1, move2)
        self.totalScore[0] += roundScore[0]
        self.totalScore[1] += roundScore[1]

    def play_game(self):
        print("Rock Paper Scissors, Go!\n")
        for round in range(numberOfRounds):
            print(f"Round {round} --")
            self.play_round()
            print(f"Score: Player One {self.totalScore[0]}, " +
                  f"Player Two {self.totalScore[1]}\n")
        gameStatus(self.totalScore)


if __name__ == '__main__':
    game = Game(HumanPlayer(), RandomPlayer())
    game.play_game()

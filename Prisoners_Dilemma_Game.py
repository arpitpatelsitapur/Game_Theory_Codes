# created by -> arpitpatel
# Mon 15 Jul 2024 23:02

# Prisoners dilemma
# example rules
#   -> if both player confess, both get 3-3 points.
#   -> if one confess one remains silent, the one who confess gets 4 points other gets 0.
#   -> if both remain silent, both get 1-1 point.

class PrisonersDilemma:
    def __init__(self, rounds):
        self._rounds = rounds  # Initialize rounds
        self.rules = [[[3, 3], [0, 4]],
                      [[4, 0], [1, 1]]]
        self.players_scores = [0, 0]

    def choices(self, player_no):
        print(f'------------ Player {player_no} --------------')
        while True:
            choice = input('Please Select:\n-> 0 for Confess\n-> 1 to Remain Silent\nChoose: ')
            if choice in ['0', '1']:
                return int(choice)
            else:
                print("Invalid choice. Please enter 0 or 1.")

    def print_rules(self):
        print('''The Rules are :
----------------------------------------------
                 | Confess  | Remain silent
-----------------|----------|-----------------
Confess          |  3,3     |   4,0
-----------------|----------|-----------------
Remain silent    |  0,4     |   1,1
----------------------------------------------''')

    def print_score(self):
        print(f'Player 1 : {self.players_scores[0]}')
        print(f'Player 2 : {self.players_scores[1]}')

    def gameplay(self):
        print(f'||||||||||||||||| ROUND {self._rounds} ||||||||||||||||||')
        choice_1 = self.choices(1)
        choice_2 = self.choices(2)
        print('*****************************')
        print('Previous score ->')
        self.print_score()
        self.players_scores[0] += self.rules[choice_1][choice_2][0]
        self.players_scores[1] += self.rules[choice_1][choice_2][1]
        print('New score ->')
        self.print_score()
        print('*****************************')

    def play(self):
        self.print_rules()
        while self._rounds > 0:
            self.gameplay()
            self._rounds -= 1

        if self.players_scores[0] > self.players_scores[1]:
            print('Player 1 Won !!!')
        elif self.players_scores[0] < self.players_scores[1]:
            print('Player 2 Won !!!')
        else:
            print('Equal score.')

    @property
    def remaining_rounds(self):
        return self._rounds


# Usage:
if __name__ == "__main__":
    rounds = int(input('Enter how many rounds you want to play: '))
    game = PrisonersDilemma(rounds)
    game.play()

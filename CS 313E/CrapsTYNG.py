import random

class Craps(object):

    def __init__(self):
        self.Craps = Craps

    def setup(self):
        self.player_bank = 1000
        self.current_wager = 0
        self.point = None
        self.odds_bet = [] # [win, lose]

    def get_player(self):
        while True:
            begin = input('Would you like to begin?\nYes or No:  ')
            begin = begin.lower()
            if begin in ['y', 'ye', 'yes', 'yeah', 'yep', 'yea']:
                player = 'yes'
                break
            elif begin in ['n', 'no', 'nop', 'nope']:
                player = 'no'
                break
            else:
                print("I don't understand your input.  Please try again.")
                continue
        return player

    def ask_for_value(question):
        """The solution for asking for a integer value without using exceptions """

        answer = ""

        while not answer.isdigit():
            answer = input(question)

            # Error message
            if not answer.isdigit():
                print("Input must be a number!")
            else:
                # Cast for answer
                return int(answer)

        return answer

    def get_wager(self):
        print("How Much Would you Like to Wager on the Pass Line?")
        print("Current Bankroll: $", self.player_bank)

        # Ask for user input
        self.current_wager = eval(input('Wager Amount: '))

    def start(self):
        phase1 = True
        while phase1:
            Craps.first_roll()
        input('done')

    def roll_dice(self):
        di_1, di_2 = random.randint(1, 6), random.randint(1, 6)
        return di_1 + di_2

    def show_bank(self):
        print('Player Bank: ${}'.format(self.player_bank))

    def calc_bank(self):
        # get player_bank
        # adjust player_bank according to result of turn
        # return adjusted player_bank
        pass

    def add_odds(self, point, answer):
        if answer in ['y', 'yes', 'yep', 'ye', 'yea', 'yeah']:
            if point == 4 or point == 10:
                odds_win, odds_lose = 10, 5  # $5 bet pays back $10
            if point == 5 or point == 9:
                odds_win, odds_lose = 7.5, 5  # $5 bet pays back $7.50
            if point == 6 or point == 8:
                odds_win, odds_lose = 6, 5  # $5 bet pays back $6
        else:
            odds_win, odds_lose = 0, 0
        self.odds_bet = [odds_win, odds_lose]

    def first_roll(self, roll):
        self.get_wager()
        if roll in [7, 11]:
            print("Winner,", self.roll_dice(), "!! Pay the Line!")
            self.player_bank = self.player_bank + self.current_wager
            print("You win $", self.current_wager, '!')
            print("Player bank is now at ${}".format(self.player_bank))
        elif roll in [2, 3, 12]:
            print("Craps,", self.roll_dice(), "Craps... Line Away.")
            self.player_bank = self.player_bank - self.current_wager
            print("You lose $", self.current_wager, '!')
            print("Player bank is now ${}.".format(self.player_bank))
        else:
            self.point = roll
            print("Point is set at {}".format(roll))

            answer = input("Would you like to place an ODDS bet?\nYes or No:  ")
            answer.lower()
            self.add_odds(roll, answer)

    def sub_roll(self, roll):
        if roll == self.point:
            self.player_bank += (5 + self.odds_bet[0])
            print("You hit the point to win the turn and add ${} to your bank!".format(
                5 + self.odds_bet[0]))
            print("Player bank is now at ${}".format(self.player_bank))
            self.point = None
        elif roll == 7:
            self.player_bank -= (5 + self.odds_bet[1])
            print("CRAP!  You hit seven and lose ${}.".format(5 + self.odds_bet[1]))
            print("Player bank is now at ${}".format(self.player_bank))
            self.point = None

    def play_game(self):
        while self.player_bank >= 25: #min bet

            action = input("Your move. Press any key to roll, 'bank' to see player bank, 'point' to ask for the point, and type 'q' or 'quit' to exit game.  ")
            action.lower()
            if action in ['q', 'quit']:
                print("You have ${} in your bank.  Thanks for playing.".format(self.player_bank))
                sys.exit()

            if action == 'bank':
                self.show_bank()
                continue
            if action == 'point':
                print("The point is currently {}".format(self.point))
                continue
            # Roll starts Here ________________________
            if action != ['q', 'quit']:
                roll = self.roll_dice()
                print("You rolled {}".format(roll))
                if self.point == None:
                    self.first_roll(roll)
                    continue
                else:
                    self.sub_roll(roll)
                    continue

            else:
                print("Invalid input.")
                continue

        print('You have ${} in your bank. You need $5 or more to play.  Sorry.'.format(
            self.player_bank))
        sys.exit()

    def __init__(self):
        self.setup()

        choice = self.get_player()
        if choice == 'yes':
            print('You have been assigned an initial bankroll of $1,000, good luck!')

        if choice == 'no':
            print("Too bad.  Perhaps another time.\nGoodbye...  ")
            sys.exit()
        self.play_game()

        print(self.player_bank)
        print(self.point)
        print(self.come_out)
        print(self.point_odds)
        sys.exit()

Craps()
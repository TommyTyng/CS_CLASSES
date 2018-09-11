#  File: Poker.py

#  Description: Playing Poker

#  Student's Name: Andrew Han

#  Student's UT EID: ah49372

#  Partner's Name: Thomas Tyng

#  Partner's UT EID: tct537

#  Course Name: CS 313E

#  Unique Number: 51335

#  Date Created: February 9th, 2018

#  Date Last Modified: February 9th, 2018

import random


class Card(object):
    RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)
    SUITS = ('C', 'D', 'H', 'S')

    def __init__(self, rank=12, suit='S'):
        if (rank in Card.RANKS):
            self.rank = rank
        else:
            self.rank = 12

        if (suit in Card.SUITS):
            self.suit = suit
        else:
            self.suit = 'S'

    def __str__(self):
        if self.rank == 14:
            rank = 'A'
        elif self.rank == 13:
            rank = 'K'
        elif self.rank == 12:
            rank = 'Q'
        elif self.rank == 11:
            rank = 'J'
        else:
            rank = self.rank
        return str(rank) + self.suit

    def __eq__(self, other):
        return (self.rank == other.rank)

    def __ne__(self, other):
        return (self.rank != other.rank)

    def __lt__(self, other):
        return (self.rank < other.rank)

    def __le__(self, other):
        return (self.rank <= other.rank)

    def __gt__(self, other):
        return (self.rank > other.rank)

    def __ge__(self, other):
        return (self.rank >= other.rank)


class Deck(object):
    def __init__(self):
        self.deck = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                card = Card(rank, suit)
                self.deck.append(card)

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        if len(self.deck) == 0:
            return None
        else:
            return self.deck.pop(0)


class Poker(object):
    def __init__(self, numHands):
        self.deck = Deck()
        self.deck.shuffle()
        self.hands = []
        numCards_in_Hand = 5

        for i in range(numHands):
            hand = []
            for j in range(numCards_in_Hand):
                hand.append(self.deck.deal())
            self.hands.append(hand)

    def play(self):
        scoreHands = []
        rankHands = []
        for i in range(len(self.hands)):
            sortedHand = sorted(self.hands[i], reverse=True)
            hand = ''
            for card in sortedHand:
                hand = hand + str(card) + ' '
            print('Player ' + str(i + 1) + ': ' + hand)

            currentScore = self.is_royal(sortedHand)
            if currentScore != 0:
                scoreHands.append(currentScore)
                rankHands.append('Player ' + str(i + 1) + ': ' + 'Royal')
                continue

            currentScore = self.is_straight_flush(sortedHand)
            if currentScore != 0:
                scoreHands.append(currentScore)
                rankHands.append('Player ' + str(i + 1) + ': ' + 'Straight Flush')
                continue

            currentScore = self.is_four_kind(sortedHand)
            if currentScore != 0:
                scoreHands.append(currentScore)
                rankHands.append('Player ' + str(i + 1) + ': ' + 'Four of Kind')
                continue

            currentScore = self.is_full_house(sortedHand)
            if currentScore != 0:
                scoreHands.append(currentScore)
                rankHands.append('Player ' + str(i + 1) + ': ' + 'Full House')
                continue

            currentScore = self.is_flush(sortedHand)
            if currentScore != 0:
                scoreHands.append(currentScore)
                rankHands.append('Player ' + str(i + 1) + ': ' + 'Flush')
                continue

            currentScore = self.is_straight(sortedHand)
            if currentScore != 0:
                scoreHands.append(currentScore)
                rankHands.append('Player ' + str(i + 1) + ': ' + 'Straight')
                continue

            currentScore = self.is_three_kind(sortedHand)
            if currentScore != 0:
                scoreHands.append(currentScore)
                rankHands.append('Player ' + str(i + 1) + ': ' + 'Three of a Kind')
                continue

            currentScore = self.is_two_pair(sortedHand)
            if currentScore != 0:
                scoreHands.append(currentScore)
                rankHands.append('Player ' + str(i + 1) + ': ' + 'Two Pair')
                continue

            currentScore = self.is_one_pair(sortedHand)
            if currentScore != 0:
                scoreHands.append(currentScore)
                rankHands.append('Player ' + str(i + 1) + ': ' + 'One Pair')
                continue
            else:
                scoreHands.append(self.is_high_card(sortedHand))
                rankHands.append('Player ' + str(i + 1) + ': ' + 'High Card')
                continue

        # print rank of each hand in game
        print()
        for i in range(len(self.hands)):
            print(rankHands[i])
        print()

        winner = max(scoreHands)
        maxList = []

        for i in range(len(scoreHands)):
            if scoreHands[i] == winner:
                maxList.append(i + 1)

        if len(maxList) > 1:
            for i in range(len(maxList)):
                print('Player ' + str(maxList[0]) + ' wins.')
                print('Player ' + str(maxList[i]) + ' ties.')
        else:
            print('Player ' + str(maxList[0]) + ' wins.')

    def is_royal(self, hand):
        h = 10
        if hand[0].rank == 14:
            for i in range(len(hand) - 1):
                if hand[i].rank - hand[i + 1].rank != 1 or hand[i].suit != hand[i + 1].suit:
                    return 0
            total = h * 13 ** 5 + hand[0].rank * 13 ** 4 + hand[1].rank * 13 ** 3 + hand[2].rank * 13 ** 2 + hand[
                                                                                                                 3].rank * 13 + \
                    hand[4].rank
            return total
        else:
            return 0

    def is_straight_flush(self, hand):
        h = 9
        for i in range(len(hand) - 1):
            if hand[i].rank - hand[i + 1].rank != 1 or hand[i].suit != hand[i + 1].suit:
                return 0
        total = h * 13 ** 5 + hand[0].rank * 13 ** 4 + hand[1].rank * 13 ** 3 + hand[2].rank * 13 ** 2 + hand[
                                                                                                             3].rank * 13 + \
                hand[4].rank
        return total

    def is_four_kind(self, hand):
        h = 8
        if hand[0].rank == hand[3].rank:
            total = h * 13 ** 5 + hand[0].rank * 13 ** 4 + hand[1].rank * 13 ** 3 + hand[2].rank * 13 ** 2 + hand[
                                                                                                                 3].rank * 13 + \
                    hand[4].rank
            return total
        if hand[1].rank == hand[4].rank:
            total = h * 13 ** 5 + hand[4].rank * 13 ** 4 + hand[1].rank * 13 ** 3 + hand[2].rank * 13 ** 2 + hand[
                                                                                                                 3].rank * 13 + \
                    hand[0].rank
            return total
        else:
            return 0

    def is_full_house(self, hand):
        h = 7
        if hand[0].rank == hand[2].rank and hand[3].rank == hand[4].rank:
            total = h * 13 ** 5 + hand[0].rank * 13 ** 4 + hand[1].rank * 13 ** 3 + hand[2].rank * 13 ** 2 + hand[
                                                                                                                 3].rank * 13 + \
                    hand[4].rank
            return result
        if hand[0].rank == hand[1].rank and hand[2].rank == hand[4].rank:
            total = h * 13 ** 5 + hand[2].rank * 13 ** 4 + hand[3].rank * 13 ** 3 + hand[4].rank * 13 ** 2 + hand[
                                                                                                                 1].rank * 13 + \
                    hand[0].rank
            return total
        else:
            return 0

    def is_flush(self, hand):
        h = 6
        for i in range(len(hand) - 1):
            if hand[i].suit != hand[i + 1].suit:
                return 0
        total = h * 13 ** 5 + hand[0].rank * 13 ** 4 + hand[1].rank * 13 ** 3 + hand[2].rank * 13 ** 2 + hand[
                                                                                                             3].rank * 13 + \
                hand[4].rank
        return total

    def is_straight(self, hand):
        h = 5
        for i in range(len(hand) - 1):
            if hand[i].rank - hand[i + 1].rank != 1:
                return 0
        total = h * 13 ** 5 + hand[0].rank * 13 ** 4 + hand[1].rank * 13 ** 3 + hand[2].rank * 13 ** 2 + hand[
                                                                                                             3].rank * 13 + \
                hand[4].rank
        return total

    def is_three_kind(self, hand):
        h = 4
        if hand[0].rank == hand[2].rank:
            total = h * 13 ** 5 + hand[0].rank * 13 ** 4 + hand[1].rank * 13 ** 3 + hand[2].rank * 13 ** 2 + hand[
                                                                                                                 3].rank * 13 + \
                    hand[4].rank
            return total
        elif hand[1].rank == hand[3].rank:
            total = h * 13 ** 5 + hand[1].rank * 13 ** 4 + hand[2].rank * 13 ** 3 + hand[3].rank * 13 ** 2 + hand[
                                                                                                                 0].rank * 13 + \
                    hand[4].rank
            return total
        elif hand[2].rank == hand[4].rank:
            total = h * 13 ** 5 + hand[2].rank * 13 ** 4 + hand[3].rank * 13 ** 3 + hand[4].rank * 13 ** 2 + hand[
                                                                                                                 0].rank * 13 + \
                    hand[1].rank
            return total
        else:
            return 0

    def is_two_pair(self, hand):
        h = 3
        if hand[0].rank == hand[1].rank and hand[2].rank == hand[3].rank:
            total = h * 13 ** 5 + hand[0].rank * 13 ** 4 + hand[1].rank * 13 ** 3 + hand[2].rank * 13 ** 2 + hand[
                                                                                                                 3].rank * 13 + \
                    hand[4].rank
            return total
        elif hand[0].rank == hand[1].rank and hand[3].rank == hand[4].rank:
            total = h * 13 ** 5 + hand[0].rank * 13 ** 4 + hand[1].rank * 13 ** 3 + hand[3].rank * 13 ** 2 + hand[
                                                                                                                 4].rank * 13 + \
                    hand[2].rank
            return total
        elif hand[1].rank == hand[2].rank and hand[3].rank == hand[4].rank:
            total = h * 13 ** 5 + hand[1].rank * 13 ** 4 + hand[2].rank * 13 ** 3 + hand[3].rank * 13 ** 2 + hand[
                                                                                                                 4].rank * 13 + \
                    hand[0].rank
            return total
        else:
            return 0

    # determine if current hand is one pair
    def is_one_pair(self, hand):
        h = 2
        if hand[0].rank == hand[1].rank:
            total = h * 13 ** 5 + hand[0].rank * 13 ** 4 + hand[1].rank * 13 ** 3 + hand[2].rank * 13 ** 2 + hand[
                                                                                                                 3].rank * 13 + \
                    hand[4].rank
            return total
        elif hand[1].rank == hand[2].rank:
            total = h * 13 ** 5 + hand[1].rank * 13 ** 4 + hand[2].rank * 13 ** 3 + hand[0].rank * 13 ** 2 + hand[
                                                                                                                 3].rank * 13 + \
                    hand[4].rank
            return total
        elif hand[2].rank == hand[3].rank:
            total = h * 13 ** 5 + hand[2].rank * 13 ** 4 + hand[3].rank * 13 ** 3 + hand[0].rank * 13 ** 2 + hand[
                                                                                                                 1].rank * 13 + \
                    hand[4].rank
            return total
        elif hand[3].rank == hand[4].rank:
            total = h * 13 ** 5 + hand[3].rank * 13 ** 4 + hand[4].rank * 13 ** 3 + hand[0].rank * 13 ** 2 + hand[
                                                                                                                 1].rank * 13 + \
                    hand[2].rank
            return total
        else:
            return 0

    def is_high_card(self, hand):
        h = 1
        total = h * 13 ** 5 + hand[0].rank * 13 ** 4 + hand[1].rank * 13 ** 3 + hand[2].rank * 13 ** 2 + hand[
                                                                                                             3].rank * 13 + \
                hand[4].rank
        return total


# start the game
def main():
    numHands = int(input('Enter number of players: '))
    while (numHands < 2 or numHands > 6):
        numHands = int(input('Enter number of players: '))
    print()
    game = Poker(numHands)
    game.play()


main()

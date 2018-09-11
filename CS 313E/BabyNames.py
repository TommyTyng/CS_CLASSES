#  File: BabyNames.py

#  Description: List of popular baby names from 1900 to now.

#  Student Name: Thomas Tyng

#  Student UT EID: tct537

#  Course Name: CS 313E

#  Unique Number: 51335

#  Date Created: 3/19/18

#  Date Last Modified: 3/23/18

import sys
import urllib.request

file = urllib.request.urlopen("http://www.cs.utexas.edu/~mitra/csSpring2018/cs313/assgn/names.txt")
names_dict = {}

# go through each line and start new key as a string and empty list for ranks
for line in file:
    line = str(line, encoding='utf8')
    line.strip('\n')
    name = ''
    ranks = []
    number = ''

    # append to name if str is a letter and to ranks if a number
    for i in line:

        if (ord(i[0]) >= 65) and (ord(i[0]) <= 122):
            name += i
        elif i == '\n':
            number = int(number)
            ranks.append(number)
            number = ''
        elif (i == ' '):
            if number != '':
                number = int(number)
                ranks.append(number)
                number = ''
        elif int(i) >= 0:
            number += i

    names_dict[name] = ranks

file.close()


class names(object):
    # Initializer
    def __init__(self):
        self.names_dict = names_dict

    # Prints options to user
    def print_menu(self):
        print(
            'The menu choices are: ' "\n\n" '1. to search for names.' "\n"'2. to display data for one name.'"\n" '3. to display all names that appear in one decade.'"\n" '4. to display all names that appear in all decades.'"\n" '5. to display all names that are more popular in every decade.'"\n" '6. to display all names that are less popular in every decade.'"\n" '7. to quit')

    # Asks user for an order
    def ask(self):
        try:
            self.choice = int(input('Enter choice: '))
        except ValueError:
            print('Enter your choice as a numeral')
            self.choice = int(input('Enter choice: '))

        self.direct()

    # Runs whichever function the user wants
    def direct(self):
        if self.choice == 1:
            self.one()
        if self.choice == 2:
            self.two()
        if self.choice == 3:
            self.three()
        if self.choice == 4:
            self.four()
        if self.choice == 5:
            self.five()
        if self.choice == 6:
            self.six()
        if self.choice >= 7:
            self.seven()

    # Option 1 in menu
    def one(self):
        if self.choice == 1:
            try:
                specific = str(input('Enter a name: '))
            except:
                specific = str(input('Enter a name: '))

            if specific not in names_dict.keys():
                print(specific + ' does not appear in any decade.')
                self.ask()
            # Make sure the minimum is not 0,if it is replace w/ 1001 and find min again
            if self.names_dict[specific]:
                ranks = self.names_dict[specific]
                if min(ranks) != 0:
                    small = min(ranks)
                    decade = 1900 + (10 * ranks.index(small))

                else:
                    for i in range(len(ranks)):
                        if ranks[i] == 0:
                            ranks[i] = 1001
                    small = ranks.index(min(ranks))

                    decade = 1900 + (10 * small)
            else:
                print(specific, 'does not appear in any decade.')
            print('The matches with their highest ranking decade are: ' + "\n" + str(specific) + ' ' + str(decade))
            self.ask()

    # Option 2 in menu
    def two(self):
        if self.choice == 2:
            specific = str(input('Enter a name: '))
            if specific not in names_dict.keys():
                print(specific + ' does not appear in any decade.')
                self.ask()

            if self.names_dict[specific]:
                ranks = self.names_dict[specific]

            print(specific, ":", end='')
            for i in ranks:
                print(i, ' ', end='')
            print()
            for i in range(len(ranks)):
                print(str(1900 + (i * 10)) + ": " + str(ranks[i]))
            self.ask()

    # Option 3 in menu
    def three(self):
        try:
            if self.choice == 3:
                decade = eval(input('Enter decade: '))
                indx = (decade - 1900) // 10
                names_list = []
                for key in self.names_dict:
                    if (self.names_dict[key].count(0) == 10) and (self.names_dict[key][indx] > 0):
                        names_list.append(key)
                names_list.sort()
                print("The names are in alphabetical:")
                for i in names_list:
                    print(i)
                self.ask()
        except:
            print('Could not retrieve data')
        finally:
            self.ask()

    # Option 4 in menu
    def four(self):
        if self.choice == 4:

            popular_names = []
            for key in names_dict:
                if self.names_dict[key].count(0) == 0 and (self.names_dict[key].count(1001) == 0):
                    popular_names.append(key)
            popular_names.sort()
            print(str(len(popular_names)), "names appear in every decade. The names are:")
            for i in popular_names:
                print(i)
            self.ask()

    # Option 5 in menu
    def five(self):

        if self.choice == 5:
            rising = []
            for key in self.names_dict:
                x = 0
                for i in range(10):
                    if self.names_dict[key][i] > self.names_dict[key][i + 1]:
                        x += 1
                if x == 10:
                    rising.append(key)
            rising.sort()
            print(str(len(rising)) + " names are more popular in every decade.")
            for i in rising:
                print(i)
            self.ask()

    # Option 6 in menu
    def six(self):
        if self.choice == 6:
            descending = []
            for key in self.names_dict:
                x = 0
                for i in range(10):
                    if self.names_dict[key][i] < self.names_dict[key][i + 1]:
                        x += 1
                if x == 10:
                    descending.append(key)
                if (x == 9) and (self.names_dict[key][10] == 0):
                    descending.append(key)
            descending.sort()
            print(str(len(descending)) + " names are less popular in every decade.")
            for i in descending:
                print(i)

            self.ask()

    # Option 7 in menu
    def seven(self):
        if self.choice >= 7:
            print('Goodbye.')
            sys.exit()


def main():
    r = names()

    r.print_menu()
    r.ask()


main()

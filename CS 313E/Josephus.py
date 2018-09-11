#  File: Josephus.py

#  Description:

#  Student Name: Andrew Han

#  Student UT EID: ah49372

#  Partner Name: Thomas Tyng

#  Partner UT EID: tct537

#  Course Name: CS 313E

#  Unique Number: 51335

#  Date Created: March 28th, 2018

#  Date Last Modified: April 2nd, 2018
class Link(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class CircularList(object):
    # Constructor
    def __init__(self):
        self.first = None

    # Insert an element (value) in the list
    def insert(self, item):
        new_link = Link(item)
        if self.first == None:
            self.first = new_link
            self.first.next = self.first
            return
        else:
            current = self.first
            while (current.next != self.first):
                current = current.next
            current.next = new_link
            current = current.next
            current.next = self.first
            return

    # Find the link with the given key (value)
    def find(self, key):
        current = self.first
        if current == None:
            return None
        else:
            if current.next == self.first and current.data == key:
                return current
        while (current.next != self.first):
            if current.data == key:
                return current
            else:
                current = current.next
        if current.data == key:
            return current
        else:
            return None

    # Delete a link with a given key (value)
    def delete(self, key):
        current = self.first
        previous = self.first
        while previous.next != self.first:
            previous = previous.next
        if current == None:
            return None
        else:
            if current.next == self.first and current.data == key:
                return current
            while (current.data != key):
                if current.next == self.first:
                    return None
                else:
                    previous = current
                    current = current.next
            if current == self.first:
                self.first = self.first.next
            previous.next = current.next
            return current

    # Delete the nth link starting from the Link start
    # Return the next link from the deleted Link
    def delete_after(self, start, n):
        starting = self.first
        deads = ""
        while start != 1:
            starting = starting.next
            start -= 1
        while starting.next != starting:
            for i in range(n - 1):
                starting = starting.next
            value = starting.data
            dead = self.delete(value)
            deads += str(dead.data) + " "
            starting = starting.next
        print(deads)
        print(starting.data)

    # Return a string representation of a Circular List
    def __str__(self):
        current = self.first
        if current == None:
            return 'The list is empty'
        tmp = str(current.data)
        tmp += '  '
        while current.next != self.first:
            tmp += str(current.next.data)
            current = current.next
            tmp += '  '
        result = tmp[0:-1]
        return result


def main():
    # open the file
    in_file = open("josephus.txt", "r")
    soldier = int(in_file.readline())
    start = int(in_file.readline())
    inc = int(in_file.readline())

    CirList = CircularList()

    for i in range(1, soldier + 1):
        CirList.insert(i)
    if CirList.first != None:
        CirList.delete_after(start, inc)
    else:
        print(CirList)


main()

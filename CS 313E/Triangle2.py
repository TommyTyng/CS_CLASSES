#  File: Triangle.py

#  Description: Returning the sum in four different algorithms

#  Student's Name: Andrew Han

#  Student's UT EID: ah49372

#  Partner's Name: Thomas Tyng

#  Partner's UT EID: tct537

#  Course Name: CS 313E

#  Unique Number: 51335

#  Date Created: March 4th 2018

#  Date Last Modified: March 9th 2018

import time


# returns the greatest path sum using exhaustive search
def exhaustive_search(grid):
    lines = len(grid)
    output = 2 ** (lines - 1)
    max = 0
    for i in range(output):
        temp = int(grid[0][0])
        index = 0
        for j in range(lines - 1):
            index += (i >> j & 1)
            temp = temp + int(grid[j + 1][index])
        if temp > max:
            max = temp
    return max


# returns the greatest path sum using greedy approach
def greedy(grid):
    lines = len(grid)
    index = 0
    total = 0

    for i in range(lines - 1):
        total += int(grid[i][index])
        if (grid[i + 1][index] > grid[i + 1][index + 1]):
            index = index
        else:
            index += 1
    total += int(grid[i + 1][index])
    return total


# returns the greatest path sum using divide and conquer (recursive) approach
def rec_search(grid, row=0, idx=0):
    num_rows = len(grid)
    if row >= num_rows:
        return 0
    else:
        a0 = rec_search(grid, row + 1, idx)
        a1 = rec_search(grid, row + 1, idx + 1)
        final = max(a0, a1) + int(grid[row][idx])

    return final


# returns the greatest path sum and the new grid using dynamic programming
def dynamic_prog(grid):
    lines = len(grid)
    for i in range(lines - 2, -1, -1):
        for j in range(i + 1):
            grid[i][j] = int(grid[i][j]) + max(int(grid[i + 1][j]), int(grid[i + 1][j + 1]))
    return grid[0][0]


# reads the file and returns a 2-D list that represents the triangle
def read_file():
    inFile = open('triangle.txt', 'r')
    lines = inFile.readline()
    lines = lines.strip()
    lines = int(lines)

    line_list = []

    for i in range(lines):
        row = inFile.readline()
        row = row.strip()
        row = row.split()
        line_list.append(row)
    return line_list


def main():
    # read triangular grid from file
    triangle = read_file()

    exhaust_total = exhaustive_search(triangle)
    ti = time.time()
    # output greates path from exhaustive search
    tf = time.time()
    del_t = tf - ti
    print("The greatest path sum through exhaustive search is", exhaust_total)

    # print time taken using exhaustive search
    print("The time taken for exhaustive search is", del_t, "seconds.")

    greedy_total = greedy(triangle)
    ti2 = time.time()
    # output greates path from greedy approach
    tf2 = time.time()

    del_t2 = tf2 - ti2
    print("The greatest path sum through greedy search is", greedy_total)

    # print time taken using greedy approach
    print("The time taken for greedy search is", del_t2, "seconds.")

    ti3 = time.time()
    # output greates path from divide-and-conquer approach
    tf3 = time.time()
    recursive_total = rec_search(triangle)
    del_t3 = tf3 - ti3
    print("The greatest path sum through recursive search is", recursive_total)

    # print time taken using divide-and-conquer approach
    print("The time taken for recursive search is ", del_t3, 'seconds.')

    ti4 = time.time()
    # output greates path from dynamic programming
    tf4 = time.time()
    dynamic_total = dynamic_prog(triangle)
    del_t4 = tf4 - ti4
    print("The greatest path sum through dynamic programming is", dynamic_total)
    # print time taken using dynamic programming
    print("The time taken for dynamic programming is ", del_t4, 'seconds.')


if __name__ == "__main__":
    main()

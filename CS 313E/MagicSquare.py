
 # File: MagicSquare.py

 # Description: Creates and checks a magic square

 # Student's Name: Daniel Greer 

 # Student's UT EID: ddg943
 
 # Partner's Name: Thomas Tyng

 # Partner's UT EID: tct537

 # Course Name: CS 313E 

 # Unique Number: 51335	

 # Date Created: 1/24/2018

 # Date Last Modified: 1/27/2018



# Populate a 2-D list with numbers from 1 to n2
def make_square (n):
    
    square = [[0 for x in range(n)] for x in range(n)]
    x = n-1
    y = int((n + 2) / 2 - 1)
    square[x][y] = 1
    
    for i in range(2, n * n + 1):
        x_old = x
        y_old = y
    
        if x == n-1:
            x = 0
            
        else:
            x += 1
    
        if y == n - 1:
            y = 0
        else:
            y += 1

        while square[x][y] != 0:
            if x == 0:
               x = n-1
            else:
               x = x_old - 1
            y = y_old 
    
        square[x][y] = i

    return square

    
# Print the magic square in a neat format where the numbers
# are right justified
def print_square ( magic_square ):

    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
        for row in magic_square]))

# Check that the 2-D list generated is indeed a magic square
def check_square(magic_square):
    
    iSize = len(magic_square[0])
    sum_list = []
    
    #Horizontal Part:
    for line in magic_square:
        h=sum(line)
        
        
    #Vertical Part:
    for col in range(iSize):
        v=(sum(line[col] for line in magic_square))
    
    #Diagonals Part
    diagonal1 = 0
    for i in range(0,iSize):
        diagonal1 +=magic_square[i][i]
     
    diagonal2 = 0
    for i in range(iSize-1,-1,-1):
        diagonal2 +=magic_square[i][i]

    print('Sum of row = ', h)
    print('Sum of column = ', v)
    print('Sum of diagonal (UR to LL) = ', diagonal1)
    print('Sum of diagonal (UL to LR) = ', diagonal2)

    


def main():
    
  # Prompt the user to enter an odd number 3 or greater
    val=int(input('Please enter an odd numger greater than 3: ' ))
    
  # Check the user input
    if val%2 == 0 or val < 3:
        val=int(input('Please enter an odd number greater than 3: '))
        
  # Create the magic square
    magic_square=make_square(val)

  # Print the magic square
    print_square(magic_square)
    
  # Verify that it is a magic square
    check_square(magic_square)
    
main()

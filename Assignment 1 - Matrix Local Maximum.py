"""
FIT2004 Assignment 1 - Finding a Local Maximum
Author: Hee Zhan Zhynn
Student ID: 31989403
Version: 2
"""

#%%Q2
def local_maximum(M): 
    """
    Returns a single pair coordinates of exactly one local maximum in a N-by-N matrix

    Precondition : Matrix are made up of distinct integers
    Postcondition: The submatrix contains the local maximum

    Input:
        An N-by-N matrix with distinct integers

    Return:
        A single pair coordinates of exactly one local maximum
     
    eg:
    M = [[1, 2, 27, 28, 29, 30, 49],
        [3, 4, 25, 26, 31, 32, 48],
        [5, 6, 23, 24, 33, 34, 47],
        [7, 8, 21, 22, 35, 36, 46],
        [9, 10, 19, 20, 37, 38, 45],
        [11, 12, 17, 18, 39, 40, 44],
        [13, 14, 15, 16, 41, 42, 43]]
    local_maximum(M)
    >>> [0, 6]

    Time complexity: 
        Best : O(N) where N is the size of matrix
        Worst: O(N) where N is the size of matrix

    Space complexity: 
        Input: O(N^2) where N is the size of matrix
        Aux  : O(1) 
    """
    firstRow = 0
    lastRow = len(M) - 1
    firstCol = 0
    lastCol = len(M) - 1

    if len(M) == 1: #only 1 item in matrix, so it is itself
        return [0,0]

    while firstRow <= lastRow: 
        midRow = (firstRow + lastRow)//2 + 1 
        midCol = (firstCol + lastCol)//2 

        max_in_row = find_max_in_row(M, midRow, firstCol, lastCol) #returns a tuple coordinates
        max_in_col = find_max_in_col(M, midCol, firstRow, lastRow) #returns a tuple coordinates

        #find max cell in vertical or horizontal
        max_value_in_row = M[max_in_row[0]][max_in_row[1]]
        max_value_in_col = M[max_in_col[0]][max_in_col[1]]

        #checks whether max is at horizontal or vertical part
        if max_value_in_row > max_value_in_col: #max is in horizontal
            max_row_cell = max_in_row[0]
            max_col_cell = max_in_row[1]
        else:
            max_row_cell = max_in_col[0]
            max_col_cell = max_in_col[1]
        
        #max_value in vertical/horizontal part
        max_value = M[max_row_cell][max_col_cell]

        own_neighbourhood = find_bigger_neighbour(M, midRow, midCol,firstRow, firstCol, lastRow, lastCol) #check if the mid itself is the biggest neighbour
        next_neighbour = find_bigger_neighbour(M, max_row_cell, max_col_cell, firstRow, firstCol, lastRow, lastCol) #a tupple coordinate of the next biggest neighbour
        next_neighbour_row = next_neighbour[0]
        next_neighbour_col = next_neighbour[1]
        next_neighbour_value = M[next_neighbour_row][next_neighbour_col]
        
        if M[midRow][midCol] == M[own_neighbourhood[0]][own_neighbourhood[1]]:
            # print(M[midRow][midCol])
            return [midRow,midCol]

        if max_value == next_neighbour_value:
            # print(max_value)
            return [max_row_cell, max_col_cell]
        
        elif next_neighbour_row < midRow:
            if next_neighbour_col < midCol: #top-left
                if lastRow == midRow and lastCol == midCol:
                    lastRow = midRow - 1
                    lastCol = midCol - 1
                else:
                    lastRow = midRow 
                    lastCol = midCol 

            else:  #top-right
                if lastRow == midRow and firstCol == midCol:
                    lastRow = midRow - 1
                    firstCol = midCol + 1
                else:
                    lastRow = midRow    
                    firstCol = midCol 

        else:
            if next_neighbour_col < midCol: #bottom-left
                if firstRow == midRow and lastCol == midCol:
                    firstRow = midRow + 1  
                    lastCol = midCol  - 1
                else:
                    firstRow = midRow   
                    lastCol = midCol  

            else:   #bottom right
                if firstRow == midRow and firstCol == midCol:
                    firstRow = midRow + 1  
                    firstCol = midCol + 1
                else:
                    firstRow = midRow  
                    firstCol = midCol 
  
    #if non-present
    return [firstRow, firstCol]

def find_max_in_row(M, row, startCol, endCol):
    '''
    Returns the coordinate of largest item in a specific row

    Precondition : list are of distint integers
    Postcondition: All items in the row has been looped through

    Input: 
        An N-by-N matrix

    Return:
        The position of column with the largest item in the given row

    M = [   [1, 2, 27, 28, 29, 30, 49],
            [3, 4, 25, 26, 31, 32, 48],
            [5, 6, 23, 24, 33, 34, 47],
            [7, 8, 21, 22, 35, 36, 46],
            [9, 10, 19, 20, 37, 38, 45],
            [11, 12, 17, 18, 39, 40, 44],
            [13, 14, 15, 16, 41, 42, 43]]
    row = 3
    firstCol = 0
    lastCol = 6

    find_max_in_row(M, row, startCol, endCol)
    >>> [3, 6]

    Time complexity: 
        Best : O(N) where N is number of items of a row in a matrix
        Worst: O(N) where N is number of items of a row in a matrix

    Space complexity: 
        Input: O(N^2) where N is the size of matrix
        Aux  : O(1)
    '''
    maxCol = startCol
    max = M[row][startCol]
    for col in range(startCol, endCol+1):
        if max < M[row][col]:
            max = M[row][col]
            maxCol = col
    return (row,maxCol)


def find_max_in_col(M, col, startRow, endRow):
    '''
    Returns the coordinate of largest item in a specific column

    Precondition : list are of distint integers
    Postcondition: All items in the col has been looped through

    Input: 
        An N-by-N matrix

    Return:
        The position of row with the largest item in the given column

    M = [   [1, 2, 27, 28, 29, 30, 49],
            [3, 4, 25, 26, 31, 32, 48],
            [5, 6, 23, 24, 33, 34, 47],
            [7, 8, 21, 22, 35, 36, 46],
            [9, 10, 19, 20, 37, 38, 45],
            [11, 12, 17, 18, 39, 40, 44],
            [13, 14, 15, 16, 41, 42, 43]]
    col = 3
    startRow = 0
    endRow = 6

    find_max_in_col(M, col, startRow, endRow)
    >>> [0, 3]

    Time complexity: 
        Best : O(N) where N is number of items of a col in a matrix
        Worst: O(N) where N is number of items of a col in a matrix

    Space complexity: 
        Input: O(N^2) where N is the size of matrix
        Aux  : O(1)
    '''
    maxRow = startRow
    max = M[maxRow][col]
    for row in range(startRow, endRow+1): 
        if max < M[row][col]:
            max = M[row][col]
            maxRow = row
    return (maxRow, col)


def find_bigger_neighbour(M, row, col, startRow, startCol, endRow, endCol):
    '''
    Return the coordinate of the largest neighbour by comparing a specific integer to the integers at immediate top, bottom and sides.

    Precondition : list are of distint integers
    Postcondition: the integer returned is the largest

    Input:
        An N-by-N matrix and the row and column position to compare with

    Return:
        The row of the largest neighbour after comparing a specific integer to the integers at immediate top and bottom rows and sides.
    
    eg:
    M = [[1, 2, 27, 28, 29, 30, 49],
        [3, 4, 25, 26, 31, 32, 48],
        [5, 6, 23, 24, 33, 34, 47],
        [7, 8, 21, 22, 35, 36, 46],
        [9, 10, 19, 20, 37, 38, 45],
        [11, 12, 17, 18, 39, 40, 44],
        [13, 14, 15, 16, 41, 42, 43]]
    row = 6
    col = 6
    startRow = 0
    startCol = 0
    endRow = 6
    endCol = 6

    find_bigger_neighbour(M, row, col, startRow, startCol, endRow, endCol)
    >>> (5, 6)

    Time complexity: 
        Best : O(1) 
        Worst: O(1) 

    Space complexity: 
        Input: O(N^2): where N is number of items of a row in a matrix
        Aux  : O(1)
    '''
    next_neighbour = (row,col)
    next_neighbour_value = M[row][col]
    if row > startRow and next_neighbour_value < M[row-1][col]:
        next_neighbour_value = M[row-1][col]
        next_neighbour = (row-1, col)

    if col > startCol and next_neighbour_value < M[row][col-1]:
        next_neighbour_value = M[row][col-1]
        next_neighbour = (row, col-1)

    if row < endRow  and next_neighbour_value < M[row+1][col]:
        next_neighbour_value = M[row+1][col]
        next_neighbour = (row+1, col)

    if col < endCol  and next_neighbour_value < M[row][col+1]:
        next_neighbour_value =  M[row][col+1]
        next_neighbour = (row, col+1)
    
    return next_neighbour
'''
    Sudoku is a logic-based, combinatorial number-placement puzzle.
    The objective is to fill a 9×9 grid with digits so that
    each column, each row, and each of the nine 3×3 subgrids that compose the grid
    contains all of the digits from 1 to 9.

    Complete the check_sudoku function to check if the given grid
    satisfies all the sudoku rules given in the statement above.
'''


def check_sudoku(grid):
    '''
        Your solution goes here. You may add other helper functions as needed.
        The function has to return True for a valid sudoku grid and false otherwise
    '''
    if row(grid) is True and col(grid) is True and dir(grid) is True:
        return True
    return False


def row(grid):
    l_1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in range(9):
        l = grid[i]
        l = sorted(l)
        if ( l[i] == l_1):
            l = col(l)
            return True
        else:
            return False
def col(grid):
    for i in range(9):
        for j in range(9):
            l.append(grid[j][i])
            # print(l)
    if ( l[i] == l_1):
        l = dir(l)
        return True
    else:
        return False
def dir(grid):
    # l_2 = []
    # for i in range(3):
    #     for j in range (3):
    #         l_2.append(l[j][i])
    # print(l_2)
    return True





def main():
    '''
        main function to read input sudoku from console
        call check_sudoku function and print the result to console
    '''
    
    # initialize empty list
    sudoku = []

    # loop to read 9 lines of input from console
    for i in range(9):
        # read a line, split it on SPACE and append row to list
        row = input().split(' ')
        sudoku.append(row)
    # call solution function and print result to console
    print(check_sudoku(sudoku))

if __name__ == '__main__':
    main()
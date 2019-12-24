print('Enter each row followed by an Enter')
print('Each blank space should be represented by a 0\n')

row_one = list(input())
if len(row_one) != 9:
    quit("Must be exacly 9 numbers")

row_two = list(input())
if len(row_two) != 9:
    quit("Must be exacly 9 numbers")
    
row_three = list(input())
if len(row_three) != 9:
    quit("Must be exacly 9 numbers")
    
row_four = list(input())
if len(row_four) != 9:
    quit("Must be exacly 9 numbers")
    
row_five = list(input())
if len(row_five) != 9:
    quit("Must be exacly 9 numbers")
    
row_six = list(input())
if len(row_six) != 9:
    quit("Must be exacly 9 numbers")
    
row_seven = list(input())
if len(row_seven) != 9:
    quit("Must be exacly 9 numbers")
    
row_eight = list(input())
if len(row_eight) != 9:
    quit("Must be exacly 9 numbers")
    
row_nine = list(input())
if len(row_nine) != 9:
    quit("Must be exacly 9 numbers")

# Checks if the board is in a valid state
def check_valid_board(board):
    # Checks each row
    for row in range(9):
        valid_row = check_valid_numbers(board[row][0])
        if not valid_row:
            return False

    # Checks each column
    for column in range(9):
        column_to_check = list()
        for row in range(9):
            column_to_check.append(board[row][0][column])
        
        valid_column = check_valid_numbers(column_to_check)
        if not valid_column:
            return False
        
    return True

# Makes sure there are not duplicate numbers
def check_valid_numbers(list_of_numbers):
    number_check = {
        "1": False,
        "2": False,
        "3": False,
        "4": False,
        "5": False,
        "6": False,
        "7": False,
        "8": False,
        "9": False,
    }

    for number in list_of_numbers:
        for i in range(1, 9):
            if int(number) == i and not number_check[str(i)]:
                number_check[str(i)] = True
                break
            elif int(number) == i and number_check[str(i)]:
                return False
            elif int(number) == 0:
                break
    
    return True

sudoku_board = [
    [row_one],
    [row_two],
    [row_three],
    [row_four],
    [row_five],
    [row_six],
    [row_seven],
    [row_eight],
    [row_nine]
]

if check_valid_board(sudoku_board):
    print('\nThe borad provided is valid')
else:
    quit('\nThe board you provided is not valid')

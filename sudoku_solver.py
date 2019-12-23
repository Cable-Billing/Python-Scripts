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

# Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column is set to 0.

# input -> a M * N matrix
# output -> nothing
# working->

# catch if the row is 1

def convert_row_col_zero(matrix):
    row_set = set()
    column_set = set()
    row_size = len(matrix)
    column_size = len(matrix[0])
    # iterate and add the row and the colomn to each respective sets
    for row in range(row_size):
        for column in range(column_size):
            if matrix[row][column] == 0:
                row_set.add(row)
                column_set.add(column)
    
    # change the whole row to 0 for each element in the row set
    for row in row_set:
        for column in range(column_size):
            matrix[row][column] = 0

    # change the whole column to 0 for each element in the column set
    for column in column_set:
        for row in range(row_size):
            matrix[row][column] = 0

matrix = [[1,2,3],[4,5,6],[7,0,9]]
print(matrix)
convert_row_col_zero(matrix)
print(matrix)
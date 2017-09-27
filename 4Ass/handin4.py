# Read the "filename" line by line. Each line is then split be the space
# between them, and each entry in the resulting list if converted to float
# and appended to the output
def read_data(filename):
    output = []
    with open(filename, "r") as f:
        for line in f:
            row = [float(x) for x in line.split(" ")] 
            output.append(row)

    return output

# Calculates the average of each coumn of the matrix, by grabbing
# each row using list comprehension, and then calculating the sum and dividing
# by the number of entries in the column, or the row number
def calc_averages(matrix):
    num_entries = len(matrix)
    col1_avg = [row[0] for row in matrix]
    col2_avg = [row[1] for row in matrix]
    return sum(col1_avg)/num_entries, sum(col2_avg)/num_entries

# Transposes the matrix, by grabbing each column like before, the placing
# them in a list, and returning them.
def transpose_data(matrix):
    col1 = [row[0] for row in matrix]
    col2 = [row[1] for row in matrix]
    return [col1, col2]

#Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
"""
21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13
"""
#It can be verified that the sum of the numbers on the diagonals is 101.

#What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
def GeneratingMatrix(n):
    return [[0 for x in range(n)] for y in range(n)]

def NoSpiralDiagonals(n):
    # n has to be odd and it will first generate nxn matrix
    i = int(n//2)
    j = int(n//2)
    final_matrix = GeneratingMatrix(n)
    value = 1    
    final_matrix[i][j] = value
    for number in range(1, n):
        for col_number in range(1, number+1):
            value += 1
            j = ((-1)**(number+1)) + j
            final_matrix[i][j] = value
        for row_number in range(1, number+1):
            i = ((-1)**(number+1)) + i
            value += 1
            final_matrix[i][j] = value
    for new_number in range(1, n):
        i = 0
        j = new_number
        value += 1
        final_matrix[i][j] = value
    return final_matrix

def SumDiagonals(n):
    final_matrix = NoSpiralDiagonals(n)
    final_sum = 0
    for i, j in zip(range(n), range(n)):
        final_sum += final_matrix[i][j]
    for i, j in zip(range(n-1, -1, -1), range(n)):
        final_sum += final_matrix[i][j] 
    return final_sum - 1

final = SumDiagonals(1001)
print(final)
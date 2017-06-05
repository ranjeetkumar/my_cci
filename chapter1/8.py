"""
Write an algorithm such that if an element in an MxN matrix is 0,
its entire row and column are set to 0
"""
def zeromatrix(M,n,m):
    row_indices = []
    col_indices = []
    m = len(M)
    n = len(M[0])
    
    for i in range(m):
        for j in range(n):
            if M[i][j] == 0:
                row_indices.append(i)
                col_indices.append(j)
                
    for i in range(n):
        for j in row_indices:
            M[j][i] = 0
    for i in range(m):
        for j in col_indices:
            M[i][j] = 0
                
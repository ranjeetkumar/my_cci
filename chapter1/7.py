"""
Given an image represented by an NxN matrix, where each pixel in the image is 4
bytes, write a method to rotate the image by 90 degrees. 
"""

def with_space_rotate90(M):
    colno = 0
    n= len(M)
    k = [[0 for i in range(n)] for i in range(n)]
    for i in range(n-1, -1, -1):
        for j in range(n):
            k[j][colno] =  M[i][j]
        colno += 1
    return k

def in_place_rotate90(M):
     n = len(M)
     for i in range(int(n/2)):
        for j in range(i,n-i-1):
            #top_left
            temp = M[j][i] 
            # top_left = bottom_left
            M[j][i] = M[n-1-i][j]
            # bottom_left = bottom_right
            M[n-1-i][j] = M[n-1-j][n-1-i] 
            #bottom_right = top_right
            M[n-1-j][n-1-i] = M[i][n-1-j] 
            #top_right = top_left
            M[i][n-1-j] = temp 
  
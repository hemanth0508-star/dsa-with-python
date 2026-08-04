'''
Given a m x n binary matrix mat, find the 0-indexed position of the row that contains the maximum count of ones, and the number of ones in that row.
In case there are multiple rows that have the maximum count of ones, the row with the smallest row number should be selected.
Return an array containing the index of the row, and the number of ones in it.
'''
mat=[[1,1,0],[0,0,1],[1,1,1]]
max_ones=0
ind=0

for i in range(len(mat)):
    count=0
    for j in range(len(mat[0])):
        if mat[i][j]==1:
            count+=1
    if count>max_ones:
        max_ones=count
        ind=i
print(ind,max_ones)
#Input: mat = [[0,1],[1,0]]
#Output: [0,1]

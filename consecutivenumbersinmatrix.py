'''
4. Consecutive numbers in matrix
You are given an m*n matrix such that n = m+1. In the given matrix,
find if any number is consecutive for 3 times either in row, column, diagonals print the num.
If there are multiple such numbers then print minimum of those numbers.
Input format
First line contains m, the number of rows
Following m lines contain n numbers
Example Input
6
2 3 4 5 6 2 4
2 3 4 7 6 7 6
2 3 5 5 5 5 2
2 3 1 1 2 1 3
1 1 1 1 9 0 3
2 3 1 1 5 1 2
Output
1
'''
m=int(input())
k=[]
res=set()
for i in range(m):
    k.append(list(map(int,input().split())))
for i in range(m):
    for j in range(m+1-2):
        if(k[i][j]==k[i][j+1]==k[i][j+2]):
            res.add(k[i][j])
for i in range(m-2):
    for j in range(m+1):
        if(k[i][j]==k[i+1][j]==k[i+2][j]):
            res.add(k[i][j])
for i in range(m-2):
    for j in range(m+1-2):
        print(k[i][j])
    print()
print(min(res))
    

n=int(input())
res=[]
for i in range(n):
    n,m=list(map(int,input().split()))
    for j in range(m-1):
        if(m!=0):
            t=(j*j)%m
            if(t==n):
                res.append(j)
                break
        else:
            res.append(-1)
            break
for i in res:
    print(i)
'''
4. Given two integers N and M, help Monk find an integer X, such that X2%M=N and 0≤X. If there are multiple values of X print smallest one. If there is no possible value of X print 1.
Note: Make sure you handle integer overflow.
Input:
First line consists of a single integer T denoting the number of test cases.
Each test case consists of a single line containing two space separated integers denoting N and M.
Output:
For each test case print the required answer.
Constraints:
1≤T≤100
0≤N<M≤106
SAMPLE INPUT
 
2
4 5
0 4
SAMPLE OUTPUT
 
2
0
Explanation
2 is the smallest positive integer such that (2×2)%5=4
'''

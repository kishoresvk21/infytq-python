'''
9. Number of sub-arrays with an odd sum
Given an array, find the number of sub-arrays whose sum is odd.
Input Format
First line contains the size of the array.
second line the list of elements, separated by space
Output Format:
print the number of sub arrays who sum is odd
Example Input
5 4 4 5 1 3
Output
12
Explanation
These are possible subarrays with odd sum:
1.5 Sum = 5 (At index 0)
2.5, 4  Sum = 9
3.5, 4, 4  Sum = 13
4.5, 4, 4, 5, 1 Sum = 19
5.4, 4, 5  Sum = 13
6.4, 4, 5, 1, 3  Sum = 17
7.4, 5  Sum = 9
8.4, 5, 1, 3 Sum = 13
9.5  Sum = 5 (At index 3)
10.5, 1, 3  Sum = 9
11.1 Sum = 1
12.3 Sum = 3
'''
n=list(map(int,input().split()))
count=0
l=[n[i:j] for i in range(len(n)) for j in range(i+1,len(n)+1)]
for i in l:
    if(sum(i)%2!=0):
        count+=1
print(count)

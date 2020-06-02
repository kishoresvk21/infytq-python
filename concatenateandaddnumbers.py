'''
7. Concatenate and Add numbers
You are given as input a string. The string contains comma separated numbers. It is guaranteed that the numbers 5 and 8 are present in this string.
Also, the number 8 always comes after 5.
You have to generate 2 numbers num1 and num2, such that:
num1 contains the sum of all numbers which do not lie between 5 and 8 in the input (exclusive of both)
num2 contains the concatenation of all numbers between 5 and 8 (inclusive of both)
Your task is to print the sum of num1 and num2.
Example Input
3,2,6,5,1,4,8,9
Output
5168
Explanation
num1 : 3+2+6+9 = 20
num2 : 5148
Output : 5248 + 20  = 5168
'''
n=list(map(int,input().split(',')))
t=n[n.index(5):n.index(8)+1]
temp=''
for i in t:
    temp+=str(i)
print(int(temp)+sum(n[:n.index(5)]+n[n.index(8)+1:]))

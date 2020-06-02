'''
10. Pronic Number
Pronic number is a number which is the product of two consecutive integers, that is, a number n is a product of x and (x+1).
Take a string in which random numbers are present and we have to find the product and the number(one is lesser and one is greater) which is already present in the string.   Let’s see the example:
E.g. Given a string contains 1203456. The multiplication of 3 and 4(one is lesser and one is greater) product become 12 and it’s present in the string. Like 4 and 5 (one is lesser and one is greater) the product is 20 and it’s present in the string and so on.
In such a way, We have to find all the numbers and in the output, we have to display the pronic numbers on a single line. Display only distinct numbers and make sure they are in sorted order.
If we haven’t found any product then print -1.
Example Input
1203456789

Output
0 2 6 12 20 56
'''
n=input()
l=[]
for i in range(len(n)-1):
    t=int(n[i]) * int(n[i+1])
    if(str(t) in n):
        l.append(t)
if(len(l)==0):
    print("-1")
else:
    for i in sorted(set(l)):
        print(i,end=' ')
        

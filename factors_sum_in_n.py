n=input().split(',')
for i in n:
    sum1=0
    if(int(i)==0):
        sum1=-1
    elif(int(i)==1):
        sum1=1
    else:
        for j in range(1,int(i)):
            if(int(i)%j==0):
                sum1+=j
    if(str(sum1) in n):
        print(i)
'''
5.For a given list of numbers find the its factors and add the factors
then if the sum of all factor is present in original list , sort it and
print it
Ex :
Input: 0,1,6
Factors 0 = 0 , sum =0
1=1 sum =1
6 =1,2,3 = sum =6
Output : 1,6
If the sum is not present in the list then return -1.
'''

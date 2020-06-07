n=input()
e=[]
o=[]
for i in n:
    if(i.isdigit()):
        if(int(i)%2==0):
            e.append(i)
        else:
            o.append(i)
res=''
if(len(e)>len(o)):
    min1=len(o)
    max1=len(e)
    m2=e
else:
    min1=len(e)
    max1=len(o)
    m2=o
if((len(e)+len(o))%2==0):
    for i in range(min1):
        res+=e[i]+o[i]
    res+="".join(m2[min1:])
else:
    for i in range(min1):
        res+=o[i]+e[i]
    res+=''.join(m2[min1:])
print(res)
'''
3.Write a python program that it should consist of special char,
numbers and chars . if there are even numbers of special chars
Then 1) the series should start with even followed by odd
Input: t9@a42&516
Output: 492561
If there are odd numbers of special chars then the output will be
starting with odd followed by even
Input:5u6@25g7#@
Output:56527
If there are any number of additional digits append them at last
'''

'''
5. Largest even number from string
Take as input a string. This string is a mixture of letters,
integers and special char. From this string, find the largest
even number that can be possibly formed after removing the duplicates.
If an even is not formed then return -1.
Example Input
infosys@337
Output
-1
Explanation
No even number can be formed

Example Input
Hello#81@21349
Output
984312
'''
n=input()
s=set()
e=set()
for i in n:
    if i.isdigit():
        s.add(int(i))
        if(int(i)%2==0):
            e.add(int(i))
if(len(e)!=0):
    s=list(sorted(s,reverse=True))
    s.remove(min(e))
    res=''
    for i in s:
        res+=str(i)
    res+=str(min(e))
    print(res)
else:
    print("-1")

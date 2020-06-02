'''
1. Unique substring of given string (python)
Given a string, we have to find the longest substring which is unique (that has no repetition) and whose size is at least 3.
If more than one substring is found with max length then we have to print the one which appeared first in the string
If no substring is present that matches the condition then we have to print -1
Example input: A@bcd1abx
Output: A@bcd1a
'''
n=input()
st=''
for i in range(len(n)):
    if(n[i] not in st):
        st+=n[i]
    else:
        break
if(st!=''):
    print(st)
else:
    print("-1")

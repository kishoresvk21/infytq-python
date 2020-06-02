'''
2. Largest palindromic substring (python)
Take as input a string. Find the longest possible substring from this string which is also a palindrome.
Example Input
dcodocir
Output
codoc
'''
n=input()
s=[n[i:j] for i in range(len(n)) for j in range(i+1,len(n)+1)]
res=''
for i in s:
    if i==i[::-1] and len(res)<len(i):
        res=i
print(res)

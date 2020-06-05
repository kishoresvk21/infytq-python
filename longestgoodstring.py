s=input().lower()
res=0
l=[s[i:j] for i in range(len(s)) for j in range(i+1,len(s)+1)]
for i in l:
    count=0
    for j in i:
        if(j in ('a','e','i','o','u')):
            count+=1
        else:
            break
    if(len(i)==count and count>res):
        res=len(i)
    
print(res)
'''
3. Little monk loves good string. Good String is a string that only contains vowels (a,e,i,o,u). Now, his teacher gave him a string S. Little monk is wondering what is the length of the longest good string which is a substring of S.
Note: Strings contains only lower case English Alphabets.
Input:
First line contains a string S, (1≤|S|≤105), where S denotes the length of the string.
Output:
Print an integer denoting the length of the longest good substring, that is substring consists of only vowels.
SAMPLE INPUT
 
abcaac

SAMPLE OUTPUT
 
2
Explanation
Longest Good String which is a substring of S is aa so the answer is 2.'''

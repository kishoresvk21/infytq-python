
'''
3. String rotation based on squares
You are given a list of strings each having 2 components to it - word and integer. These 2 components are separated by :.
If the square of digits in the number component is even, then you must rotate the word to the right by 1
If the square of digits in the number component is odd, then you must rotate the word to the left by 2
Finally, print the rotated word.
Example Input
rhdt:246,ghftd:1246
Output
	trhd
	ftdgh
Explanation
2*2+4*4+6*6 = 56 which is even so rotate rhdt --> trhd
1*1+2*2+4*4+6*6 = 57 which is odd so rotate ghftd --> ftdgh
'''

for i in input().split(','):
    i=i.split(':')
    sum=0
    for j in i[1]:
        sum+=int(j)
    if(sum%2==0):
        print(i[0][-1]+i[0][:-1])
    else:
        print(i[0][2:]+i[0][:2])



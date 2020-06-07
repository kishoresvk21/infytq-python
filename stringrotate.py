for i in input().split(','):
    j,k=i.split(':')
    sum1=0
    for i in k:
        sum1+=int(i)*int(i)
    if(sum1%2==0):
        print(j[-1]+j[:-1])
    else:
        print(j[2:]+j[:2])
'''
4.String rotation
Input rhdt:246,ghftd:1246
Expl :here every string is associated with the number sep by : if
sum of squares of digits is even then rotate the string by 1 if
square of digits is odd then rotate the string left by 2 position
2*2+4*4+6*6=56 which is even so rotate rhdt --->trhd
1*1+2*2+4*4+6*6=57 which is odd then rotate string by 2 at left
“ghftd” op: ftdgh
'''

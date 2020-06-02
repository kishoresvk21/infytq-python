'''
8. Reverse a string except for special characters
Your task here is to take input a string and reverse it. However, you should reverse only the normal alphabets. The special characters should be in their original positions.
	Example Input
	
	sd&hg#j
	
	Output
	jg&hd#s
'''
n=input()
str1=''
l=[]
for i in n:
    if(i.isalnum()):
        str1+=i
    else:
        l.append(n.index(i))
str1=str1[::-1]
res=''
count=0
for i in range(len(n)):
    if(i in l):
        res+=n[i]
    else:
        res+=str1[count]
        count+=1
print(res)

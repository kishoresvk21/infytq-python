n=input()
dict1={'(':')','{':'}','[':']'}
count=0
st=[]
t=0
res=0
for i in range(len(n)):
    res+=1
    if(n[i] in dict1.keys()):
        count+=1
        st.append(n[i])
    else:
        if(dict1[st[-1]]==n[i]):
            count-=1
            st=st[:-1]
        else:
            t=1
            print(res)
            break
        
if(len(st)==0 and count==0):
    print(0)
if(t==0):
    print(res+1)
'''
1.Given a string of brackets (, ), {, }, [, ], find the position in the string where the orders of brackets breaks.
I/p: ())

O/p: 3

I/p: (){[]}(

O/p: 8
'''

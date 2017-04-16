import itertools
list=[]
N,Q=map(int,raw_input().split())
s=raw_input()
s=''.join(s.split())
ln=len(s)
for j in range(ln):
    for i in itertools.combinations(s,j):
        list.append(''.join(i))
list.append(s)
for i in range(1,len(list)):
    list[i]=int(max(list[i]))
list[0]=0
while(Q>0):
    opnd,opr=map(str,raw_input().split())
    Q-=1
print list

inp=input()
inp= [int(i) for i in inp.split(",")]
ans={}
j=0
sum=0
for i in inp:
    sum=sum+i
    ans[j]=sum
    j+=1

print(ans)
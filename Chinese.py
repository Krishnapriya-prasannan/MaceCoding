n=int(input())
dl=list(map(int,input().split()))
nl=list(map(int,input().split()))
ex=int(input())
for i in range(len(dl)-1):
    for j in range(i+1,len(dl)):
        if(dl[i]>dl[j]):
            temp=dl[i]
            dl[i]=dl[j]
            dl[j]=temp
for i in range(len(nl)-1):
    for j in range(i+1,len(nl)):
        if(nl[i]>nl[j]):
            temp=nl[i]
            nl[i]=nl[j]
            nl[j]=temp


m={}
sum1=0
j=n-1
for i in range(n):
    m[i]=dl[i]+nl[j]
    j-=1
for i in range(len(m)):
    if m[i]>ex:
        sum1+=m[i]-ex
print(sum1*100)

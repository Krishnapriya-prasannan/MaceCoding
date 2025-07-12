n,m=list(map(int,input().split()))
k=list(map(int,input().split()))

max1=0
for i in range(len(k)-1):
    for j in range(i+1,len(k)):
        if(k[i]>k[j]):
            temp=k[i]
            k[i]=k[j]
            k[j]=temp
for i in range(n-m,n):
    max1+=k[i]
    
    
print(max1)

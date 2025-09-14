n,h=map(int,input().split())
a=list(map(int,input().split()))
ans=0
for height in a:
  if height<=h:
    ans+=1
  else:
    ans+=2
print(ans)      
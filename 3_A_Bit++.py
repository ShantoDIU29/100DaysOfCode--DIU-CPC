n=int((input().strip()))
x=0
for i in range(n):
  s=input().strip()
  if "++" in s:
    x+=1
  else:
    x-=1
print(x)    
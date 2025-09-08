k,n,w=map(int,input().split())
t_cost=0
for i in range(1,w+1):
  b_cost=i*k
  t_cost+=b_cost
borrow=t_cost-n
if borrow<=0:
  print("0")
else:
    print(borrow)  

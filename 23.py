guest=input().strip()
host=input().strip()
pile=input().strip()

combind=guest+host
if sorted(combind)==sorted(pile):
    print("YES")
else:
   print("NO")
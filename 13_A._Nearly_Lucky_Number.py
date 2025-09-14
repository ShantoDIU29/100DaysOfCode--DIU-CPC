n = input().strip()
 
count = 0
for d in n:
    if d == '4' or d == '7':
        count += 1
 
count_str = str(count)
is_lucky = True
if count == 0:
    is_lucky = False
else:
    for c in count_str:
        if c != '4' and c != '7':
            is_lucky = False
            break
 
if is_lucky:
    print("YES")
else:
    print("NO")
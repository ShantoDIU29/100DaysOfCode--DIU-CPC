n = int(input())
bills = [100, 20, 10, 5, 1]
count = 0
 
for b in bills:
    count += n // b
    n = n % b
 
print(count)
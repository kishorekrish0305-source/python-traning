n = int(input())
a = list(map(int, input().split()))

even = 0
odd = 0

for i in range(n):
    if i % 2 == 0:
        even = even + a[i]
    else:
        odd = odd + a[i]

print(even, odd)

n = int(input())
a = list(map(int, input().split()))

maximum = a[0]

for i in a:
    if i > maximum:
        maximum = i

print(maximum)

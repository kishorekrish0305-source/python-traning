n = int(input())
a = list(map(int, input().split()))

minimum = a[0]

for i in a:
    if i < minimum:
        minimum = i

print(minimum)

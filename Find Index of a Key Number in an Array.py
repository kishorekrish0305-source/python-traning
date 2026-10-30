n = int(input())
a = list(map(int, input().split()))
key = int(input())

index = -1

for i in range(n):
    if a[i] == key:
        index = i
        break

print(index)

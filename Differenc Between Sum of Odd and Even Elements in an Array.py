n = int(input())
a = list(map(int, input().split()))

odd = 0
even = 0

for i in a:
    if i % 2 == 0:
        even = even + i
    else:
        odd = odd + i

print(odd - even)

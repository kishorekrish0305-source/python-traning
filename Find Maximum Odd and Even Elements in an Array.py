n = int(input())
a = list(map(int, input().split()))

even = None
odd = None

for i in a:
    if i % 2 == 0:
        if even == None or i > even:
            even = i
    else:
        if odd == None or i > odd:
            odd = i

print(even)
print(odd)

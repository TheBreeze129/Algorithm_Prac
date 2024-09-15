N = int(input())
s = 0
i = 0
while s <= N:
    i += 1
    s += i
print(1 if N==1 else i-1)
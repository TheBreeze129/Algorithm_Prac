a,b = list(map(int,input().split()))
ans = 1
while b != a:
    if b>a and b%2 == 0:
        b = b // 2
        ans = ans + 1
        
    elif b>a and str(b)[-1] == "1":
        b = int(str(b)[:-1])
        ans = ans + 1
    
    else:
        ans = -1
        break

print(ans)
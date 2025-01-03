Min, Max = map(int,input().split())

cnt = Max-Min+1
nums = [True] * (Max-Min + 1)

for i in range(2,int(Max**0.5)+1):
    for j in range((Min//(i*i))*(i*i),Max+1,i*i):
        if j-Min >= 0 and nums[j-Min]: 
            cnt -= 1
            nums[j-Min] = False
print(cnt)
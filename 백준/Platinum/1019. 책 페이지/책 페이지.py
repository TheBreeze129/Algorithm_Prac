nums = [0 for _ in range(10)]
N = input()
k = len(N)
for x in N:
    k -= 1
    for i in range(int(x)):
        nums[i] += 10**k
        for j in range(10):
            if k > 0:
                nums[j] += (10**(k-1))*k
    nums[0] -= 10**k
    if k > 0:
        nums[int(x)] += (int(''.join(N[-k:]))+1)
    else:
        nums[int(x)] += 1
print(*nums)
def check(arr):
    temp_max = 1
    for line in arr:
        prev = line[0]
        temp_n = 1
        for i in line[1:]:
            if prev == i:
                temp_n += 1
            else:
                temp_max = max(temp_n, temp_max)
                prev = i
                temp_n = 1
            temp_max = max(temp_n, temp_max)
    return temp_max

def check_transpose(arr):
    temp_max = 1
    for i in range(len(arr)):
        prev = arr[0][i]
        temp_n = 1
        for j in range(1, len(arr)):
            if prev == arr[j][i]:
                temp_n += 1
            else:
                temp_max = max(temp_n, temp_max)
                prev = arr[j][i]
                temp_n = 1
            temp_max = max(temp_n, temp_max)
    return temp_max

N = int(input())
arr = [list(input()) for _ in range(N)]
max_n = check(arr)
for i in range(N-1):
    for j in range(N):
        arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
        max_n = max(check(arr), check_transpose(arr), max_n)
        arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
        arr[j][i], arr[j][i+1] = arr[j][i+1], arr[j][i]
        max_n = max(check(arr), check_transpose(arr), max_n)
        arr[j][i], arr[j][i+1] = arr[j][i+1], arr[j][i]
print(max_n)
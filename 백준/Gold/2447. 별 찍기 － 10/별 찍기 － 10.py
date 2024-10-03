def rec(N):
    if N == 1:
        return "*"
    temp = rec(N//3).split("\n")
    result = ""
    for i in temp:
        result += (i*3+"\n")
    for i in temp:
        result += i
        result += (" "*len(i))
        result += (i + "\n")
    for i in temp:
        result += (i*3+"\n")
    return result[:-1]
N = int(input())
print(rec(N))
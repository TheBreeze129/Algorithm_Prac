def solution(s):
    if s[0] == ")" or s[-1] == "(":
        return False
    c = 0
    for i in s:
        if i == "(":
            c += 1
        elif i == ")":
            c -= 1
        if c < 0:
            return False
    return c == 0
        
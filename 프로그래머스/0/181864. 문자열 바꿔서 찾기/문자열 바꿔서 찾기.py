def solution(myString, pat):
    return int(pat in "".join(list(map(lambda x : 'B' if x=='A' else 'A', list(myString)))))
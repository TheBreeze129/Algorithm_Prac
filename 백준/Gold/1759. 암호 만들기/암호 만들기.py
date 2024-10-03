from itertools import combinations
L, C = map(int, input().split())
chars_comb = list(map(lambda x: "".join(x),combinations(sorted(input().split()), L)))
for i in chars_comb:
    cnt = i.count('a') + i.count('e') + i.count('i') + i.count('o') + i.count('u')
    if cnt >= 1 and cnt <= (len(i) - 2):
        print(i)
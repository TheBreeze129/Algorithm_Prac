N = int(input())
evens = []
odds = []
for i in map(int, input().split()):
    if i%2==0:
        evens.append(i)
    else:
        odds.append(i)
if len(evens)==0 and len(odds) == 1:
    print(0)
else:
    all = sum(evens) + sum(odds)
    if len(odds) % 2 != 0:
        all -= min(odds)
    print(all)
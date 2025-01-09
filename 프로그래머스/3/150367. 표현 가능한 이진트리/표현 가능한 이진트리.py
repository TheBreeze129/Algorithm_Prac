# 1 -> 0
# 3 -> 1
# 7 -> 3
# 15 -> 7

def check(numlist):
    mid = len(numlist) // 2
    if sum(numlist) == 0:
        return True
    elif numlist[mid] == 1:
        if check(numlist[:mid]) and check(numlist[mid+1:]):
            return True
    return False
        

def solution(numbers):
    answer = []
    for i in numbers:
        num = list(map(int, str(bin(i))[2:]))
        max_caninsert = len(num)-1
        floor = 1
        max_nodenum = 1
        while len(num) > max_nodenum:
            max_nodenum += (2**floor)
            floor += 1
        max_caninsert -= (max_nodenum-(len(num)))
        num = [0 for _ in range(max_nodenum-len(num))] + num
        if check(num):
            answer.append(1)
            continue
        flag = False
        while max_caninsert >= (2**floor):
            num = [0 for _ in range(2**floor)] + num
            max_caninsert -= (2**floor)
            floor += 1
            if check(num):
                answer.append(1)
                flag = True
                break
        if not flag:
            answer.append(0)
        
    return answer
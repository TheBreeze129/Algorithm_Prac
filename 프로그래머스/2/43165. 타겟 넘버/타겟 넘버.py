def solution(numbers, target):
    sums = [0]
    for i in numbers:
        sums = [x+i for x in sums] + [x-i for x in sums]
    return sums.count(target)
def solution(nums):
    n = len(nums)
    setnums = set(nums)
    if(len(setnums)>=n/2):
        return n/2
    else:
        return len(setnums)
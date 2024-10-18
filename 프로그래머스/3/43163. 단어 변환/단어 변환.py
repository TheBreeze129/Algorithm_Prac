def check(a, b):
    cnt = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            cnt += 1
            if cnt == 2:
                return False
    if cnt:
        return True
    return False

def solution(begin, target, words):
    answer = 0
    ws = {begin}
    while answer <= len(words):
        answer += 1
        temp = set()
        for w in ws:
            temp.update({word for word in words if check(w, word)})
        ws = temp
        if target in ws:
            break
    if answer > len(words):
        answer = 0
    return answer
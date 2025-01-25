def solution(myString):
    ans = ''
    for alp in myString:
        if alp < 'l':
            ans += 'l'
        else:
            ans += alp
    return ans
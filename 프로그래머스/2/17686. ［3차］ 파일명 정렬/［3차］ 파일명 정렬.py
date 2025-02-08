def split(filename):
    flag = False
    HEAD = ""
    NUMBER = ""
    tailstart = 0
    for i in range(len(filename)):
        if filename[i].isdecimal():
            flag = True
            NUMBER += filename[i]
        elif flag:
            tailstart = i
            break
        else:
            HEAD += filename[i]
    return HEAD.lower(), int(NUMBER), filename[tailstart:]
                

def solution(files):
    answer = []
    splitted = []
    for ind, data in enumerate(files):
        splitted.append((ind, *split(data)))
    splitted.sort(key=lambda x:(x[1], x[2]))
    for i in splitted:
        answer.append(files[i[0]])
    return answer
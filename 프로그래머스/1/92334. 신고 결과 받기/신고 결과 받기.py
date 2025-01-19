def solution(id_list, report, k):
    answer = []
    rep_count = {}
    mail_count = {}
    for i in id_list:
        rep_count[i] = [0,[]] #신고횟수, 신고자명단
        mail_count[i] = 0
    for i in report:
        spi = i.split(' ')
        if(spi[0] not in rep_count[spi[1]][1]):
            rep_count[spi[1]][0] = rep_count[spi[1]][0] + 1
            rep_count[spi[1]][1].append(spi[0])
    for i in rep_count:
        if(rep_count[i][0]>=k):
            for l in rep_count[i][1]:
                mail_count[l] = mail_count[l] + 1
    return list(mail_count.values())
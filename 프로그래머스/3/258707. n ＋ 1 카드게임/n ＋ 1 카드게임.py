def solution(coin, cards):
    answer = 0
    onhand = cards[:len(cards)//3]
    TARGET = len(cards) + 1
    canbuy = []
    idx = len(onhand)-2
    alive = True
    while alive and len(onhand) > 0:
        idx += 2
        canbuy.extend(cards[idx:idx+2])
        alive = False
        for card in onhand: # 내 손에꺼 내고 버틴다
            if (TARGET-card) in onhand:
                onhand.remove(card)
                onhand.remove(TARGET-card)
                alive = True
                break
        if alive:
            answer += 1
            continue
        if coin < 1:
            break
        
        # 살 수 있는 것 중에 한장 사서 버틴다
        for card in onhand:
            if (TARGET - card) in canbuy:
                onhand.remove(card)
                canbuy.remove(TARGET - card)
                coin -= 1
                alive = True
                break
        
        if alive:
            answer += 1
            continue
        if coin < 2:
            break
        
        # 살 수 있는 것 중에 두장 사서 버린다   
        for card in canbuy:
            if (TARGET - card) in canbuy:
                canbuy.remove(card)
                canbuy.remove(TARGET-card)
                coin -= 2
                alive = True
                break
        if alive:
            answer += 1
        
    return answer+1
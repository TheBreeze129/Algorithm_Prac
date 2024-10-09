from collections import deque

# 악세서리로 인한 공격력 증가는 미리 써버리자
def RPG_Extreme():
    global NAME , NOW_HP,MAX_HP,DEF,ATT,ATT_Accessories,DEF_Accessories,EXP,LV,Player_Accessories,y,x,Answer

    if graph[y][x] == "&":
        NAME,W, A, H, E = Monster[(y+1, x+1)][0],Monster[(y+1, x+1)][1], Monster[(y+1, x+1)][2], Monster[(y+1, x+1)][3], Monster[(y+1, x+1)][4]  # W-공격력 , A-방어력 , H-최대 체력 , E-죽였을때 경험치
        Battle_Turn=0

        while True:
            Battle_Turn+=1
            Player_Damage=max(1,(ATT+ATT_Accessories)-A)
            Monster_Damage=max(1,W-(DEF+DEF_Accessories))
            if "CO" in Player_Accessories and "DX" in Player_Accessories and Battle_Turn==1:
                Player_Damage=max(1,3*(ATT+ATT_Accessories)-A)
            elif "CO" in Player_Accessories and "DX" not in Player_Accessories and Battle_Turn==1:
                Player_Damage = max(1, 2 * (ATT + ATT_Accessories) - A)

            H-=Player_Damage
            if H<=0:
                if "HR" in Player_Accessories:
                    NOW_HP = min(NOW_HP + 3, MAX_HP)
                if "EX" in Player_Accessories:
                    EXP+=int(1.2 * E)
                elif "EX" not in Player_Accessories:
                    EXP += E
                if EXP >= 5 * LV:
                    LV += 1 ; EXP = 0 ; MAX_HP += 5 ; NOW_HP = MAX_HP ; ATT += 2 ; DEF += 2
                graph[y][x] = '.'
                break
            NOW_HP-=Monster_Damage

            if NOW_HP<=0:
                if "RE" in Player_Accessories:
                    NOW_HP = MAX_HP
                    y, x = start[0][0], start[0][1]
                    Player_Accessories.remove("RE")
                else:
                    NOW_HP=0
                    Answer=0
                break



    elif graph[y][x] == "B":
        T, S = Accessories[(y+1, x+1)][0], Accessories[(y+1, x+1)][1]
        if T == "W":
            ATT_Accessories = int(S)
        elif T == "A":
            DEF_Accessories = int(S)
        elif T == "O":
            if len(Player_Accessories) < 4:
                if S not in Player_Accessories:
                    Player_Accessories.append(S)
        graph[y][x] = "."

    elif graph[y][x] == "^":
        if "DX" in Player_Accessories:
            NOW_HP -= 1
        elif "DX" not in Player_Accessories:
            NOW_HP -= 5
        if NOW_HP <= 0:
            if "RE" in Player_Accessories:
                NOW_HP = MAX_HP
                y, x = start[0][0], start[0][1]
                Player_Accessories.remove("RE")
            else:
                NOW_HP = 0  # 종료 조건
                Answer=2

    elif graph[y][x] == "M":

        NAME,W, A, H, E = Monster[(y+1, x+1)][0],Monster[(y+1, x+1)][1], Monster[(y+1, x+1)][2], Monster[(y+1, x+1)][3], Monster[(y+1, x+1)][4]  # W-공격력 , A-방어력 , H-최대 체력 , E-죽였을때 경험치

        Battle_Turn = 0
        while True:
            Battle_Turn += 1
            Player_Damage = max(1, (ATT + ATT_Accessories) - A)
            Monster_Damage=max(1,W-(DEF+DEF_Accessories))

            if "CO" in Player_Accessories and "DX" in Player_Accessories and Battle_Turn == 1:
                Player_Damage = max(1, 3 * (ATT + ATT_Accessories) - A)
            elif "CO" in Player_Accessories and "DX" not in Player_Accessories and Battle_Turn == 1:
                Player_Damage = max(1, 2 * (ATT + ATT_Accessories) - A)
            if "HU" in Player_Accessories and Battle_Turn==1:
                NOW_HP=MAX_HP
                H-=Player_Damage
                Player_Damage = max(1, (ATT + ATT_Accessories) - A)
            H -= Player_Damage
            if H<=0:
                if "HR" in Player_Accessories:
                    NOW_HP = min(NOW_HP + 3, MAX_HP)
                if "EX" in Player_Accessories:
                    EXP+=int(1.2 * E)
                elif "EX" not in Player_Accessories:
                    EXP += E
                if EXP >= 5 * LV:
                    LV += 1 ; EXP = 0 ; MAX_HP += 5 ; NOW_HP = MAX_HP ; ATT += 2 ; DEF += 2
                Answer=1
                graph[y][x]='.'
                break
            NOW_HP -= Monster_Damage

            if NOW_HP <= 0:
                if "RE" in Player_Accessories:
                    NOW_HP = MAX_HP
                    y, x = start[0][0], start[0][1]
                    Player_Accessories.remove("RE")
                else:
                    NOW_HP = 0
                    Answer=0
                break
    elif graph[y][x] == "@":  # 주인공이 있던 칸이면 그냥 넘어감
        pass

N,M=map(int,input().split())
graph=[ list(input()) for i in range(N)]

Move=deque(list(input()))

Monster={} ; Accessories={} ; Monster_count=0 ; Accessories_count=0 ; start=[]
for i in range(N):
    for j in range(M):
        if graph[i][j]=="&" or graph[i][j]=="M":
            Monster_count+=1
        elif graph[i][j]=="B":
            Accessories_count+=1
        elif graph[i][j]=="@":
            start=[[i,j]]

for i in range(Monster_count):
    Monster_Y,Monster_X,NAME,W,A,H,E=input().split() #W-공격력 , A-방어력 , H-최대 체력 , E-죽였을때 경험치
    Monster_Y=int(Monster_Y) ; Monster_X=int(Monster_X) ; W=int(W) ; A=int(A) ; H=int(H) ; E=int(E)
    Monster[(Monster_Y,Monster_X)]=[NAME,W,A,H,E] #몬스터의 체력은 변할수 있으므로 저장은 리스트로한다.

for i in range(Accessories_count):
    """
    T='W'일때 공격력이 S 인 무기장착 , T='A' 인 경우  S인 방어구 장착
    T='O' 인 경우 장신구 장착
    """
    Accessories_Y,Accessories_X,T,S=input().split()
    Accessories_Y=int(Accessories_Y) ; Accessories_X=int(Accessories_X)
    if T=='W' or T=='A':
        S=int(S)
    Accessories[(Accessories_Y,Accessories_X)]=(T,S)

y,x=start[0][0],start[0][1]
LV=1 ; NOW_HP=20 ; MAX_HP=20 ; ATT=2 ; DEF=2 ; EXP=0 # 레벨 , 현재체력 , 최대체력 ,공격력 , 방어력 , 경험치

# 경험치 : 처음엔 레벨 1이며, 레벨 N에서 N+1이 되기 위한 필요 경험치는 5×N이다.
ATT_Accessories=0 ; DEF_Accessories=0 #무기 , 방어구
Player_Accessories=[] #플레이어의 악세서리 도구함 , 최대 4개까지 장착 가능

Answer=-1 # 모든 커맨드를 수행후 죽었거나 보스를 이기지 않았을 경우
count=0 # 턴 횟수 저장변수
while Move:
    count+=1
    Keyboard=Move.popleft()
    if Keyboard=="R" and 0<=x+1<M and graph[y][x+1]!="#":
        x+=1
        RPG_Extreme()
    elif Keyboard=="L" and 0<=x-1<M and graph[y][x-1]!="#":
        x-=1
        RPG_Extreme()
    elif Keyboard=="U" and 0<=y-1<N and graph[y-1][x]!="#":
        y-=1
        RPG_Extreme()
    elif Keyboard=="D" and 0<=y+1<N and graph[y+1][x]!="#":
        y+=1
        RPG_Extreme()
    else:
        if graph[y][x]=="^":
            if "DX" in Player_Accessories:
                NOW_HP -= 1
            elif "DX" not in Player_Accessories:
                NOW_HP -= 5
            if NOW_HP <= 0:
                if "RE" in Player_Accessories:
                    NOW_HP = MAX_HP
                    y, x = start[0][0], start[0][1]
                    Player_Accessories.remove("RE")
                else:
                    NOW_HP = 0  # 종료 조건
                    Answer=2
                    graph[start[0][0]][start[0][1]] = '.'
                    break

    if Answer==0: #몬스터한테 뒤졌을 경우  , 전투의 결과로 사망했을 경우 S는 몬스터의 이름, 가시 함정에 의해 사망했을 경우 S는 “SPIKE TRAP” 이 된다.
        graph[start[0][0]][start[0][1]] = '.'
        break
    elif Answer==1: #보스 이겼을 경우
        graph[start[0][0]][start[0][1]] = '.'
        graph[y][x] = '@'
        break
    elif Answer==2: #트랩에 뒤졌을 경우
        graph[start[0][0]][start[0][1]] = '.'
        break
if Answer==-1:
    graph[start[0][0]][start[0][1]] = '.'
    graph[y][x] = '@'
for i in graph:
    print(''.join(i).rstrip())
print("Passed Turns : %d"%(count))
print("LV : %d"%(LV))
print("HP : %d/%d"%(NOW_HP,MAX_HP))
print("ATT : %d+%d"%(ATT,ATT_Accessories))
print("DEF : %d+%d"%(DEF,DEF_Accessories))
print("EXP : %d/%d"%(EXP ,5*LV))
if Answer==1:
    print("YOU WIN!")
elif Answer==0:
    print("YOU HAVE BEEN KILLED BY %s.."%(NAME))# 죽인 사람 이름
elif Answer==2:
    print("YOU HAVE BEEN KILLED BY SPIKE TRAP..")
elif Answer==-1:
    print("Press any key to continue.")
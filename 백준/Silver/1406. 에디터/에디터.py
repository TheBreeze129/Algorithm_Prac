import sys
input = sys.stdin.readline
edit = list(input().rstrip())
edit_2 = []
N = int(input())
for _ in range(N):
    cmd = input().rstrip()
    if cmd[0] == 'P':
        edit.append(cmd[2])
    elif cmd == 'L' and edit:
            edit_2.append(edit.pop())
    elif cmd == "D" and edit_2:
        edit.append(edit_2.pop())
    elif cmd == 'B' and edit:
        del edit[-1]
edit_2.reverse()
print("".join(edit)+"".join(edit_2))
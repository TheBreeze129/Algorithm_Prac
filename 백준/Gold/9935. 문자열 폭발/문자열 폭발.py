import sys
input = sys.stdin.readline
input_str = input().rstrip()
boom = input().rstrip()
stack = []
boom_len = len(boom)

for i in range(len(input_str)):
    stack.append(input_str[i])
    if ''.join(stack[-boom_len:]) == boom:
        for _ in range(boom_len):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')
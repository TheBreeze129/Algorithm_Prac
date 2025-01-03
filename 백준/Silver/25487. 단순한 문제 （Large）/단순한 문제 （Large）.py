import sys
input = sys.stdin.readline
[print(min(list(map(int, input().split())))) for _ in range(int(input()))]
import sys
import heapq
input = sys.stdin.readline
N = int(input())
lessons = [tuple(map(int, input().split())) for _ in range(N)]
lessons.sort()
room = []
heapq.heappush(room, lessons[0][1])

for i in range(1, N):
    if lessons[i][0] >= room[0]:
        heapq.heappop(room)
    heapq.heappush(room, lessons[i][1])

print(len(room))

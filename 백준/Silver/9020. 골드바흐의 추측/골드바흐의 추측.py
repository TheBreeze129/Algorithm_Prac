import sys
import math
input = sys.stdin.readline

N = int(input())

def is_prime_number(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

for _ in range(N):
    T = int(input())
    K = T//2
    M = 0
    while True:
        if is_prime_number(K-M) and is_prime_number(K+M):
            print(K-M, K+M)
            break
        M += 1
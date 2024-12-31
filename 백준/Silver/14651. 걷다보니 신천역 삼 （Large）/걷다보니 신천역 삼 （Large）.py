import sys 
N = int(sys.stdin.readline())
if N == 1:
    print(0)
else:
    print((2 * (3**(N-2)))%1000000009)

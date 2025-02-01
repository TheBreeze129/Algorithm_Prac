from math import sqrt

N = int(input())
K = N

while True:
    temp = sqrt(K)
    if temp == int(temp):
        break
    K -= 1

col = int(sqrt(K))
row = N//col
if N%col != 0:
    row += 1
if col == 1:
    col += 1
if row == 1:
    col += 1
print(2*(row+col-2))

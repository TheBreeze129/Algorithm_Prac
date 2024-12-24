import math

def is_primenum(x):
    for i in range (2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

print("Yes" if is_primenum(int(input())) else "No")
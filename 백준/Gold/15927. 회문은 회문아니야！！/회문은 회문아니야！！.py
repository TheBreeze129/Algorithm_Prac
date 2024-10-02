def palindrome(i):
    for j in range(len(i)//2):
        if i[j] != i[len(i)-1-j]:
            return False
    return True

input_str = input()
if not palindrome(input_str):
    print(len(input_str))
elif input_str.count(input_str[0]) == len(input_str):
    print(-1)
else:
    print(len(input_str)-1)
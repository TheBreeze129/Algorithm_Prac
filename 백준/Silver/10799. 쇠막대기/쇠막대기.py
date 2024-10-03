s = input()
st = [0]
r = []
cnt = 0
for i in range(1, len(s)):
    if s[i] == "(":
        st.append(i)
    elif s[i-1] == "(":
        del st[-1]
        r.append(i)
    elif len(st) != 0:
        for rasor in r:
            if st[-1] < rasor and rasor < i:
                cnt += 1
        cnt += 1
        del st[-1]
print(cnt)
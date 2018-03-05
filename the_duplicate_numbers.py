s, new_s = [int(i) for i in input().split()], []
for i in range(0, len(s)):
    n = s.count (s[i])
    if n > 1 :
        new_s.append(s[i])
for f in set(new_s):
    print(f, end = ' ')
word = input()
al = [-1] * 26

for i in range(len(word)):
    if al[ord(word[i]) - 97] == -1:
        al[ord(word[i]) - 97] = i

print(*al)
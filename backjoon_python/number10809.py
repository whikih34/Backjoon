word = input()

# 알파벳 개수만큼의 리스트 만들기, 초기값은 -1
al = [-1] * 26

for i in range(len(word)):
    # 소문자 'a'의 아스키 코드 = 97
    # 해당 알파벳의 아스키 코드에 97을 빼면 0~25 중 하나에 대응됨, al의 인덱스 값에 대응
    # 즉, a는 0, z는 25에 대응됨
    if al[ord(word[i]) - 97] == -1:
        al[ord(word[i]) - 97] = i

print(*al)
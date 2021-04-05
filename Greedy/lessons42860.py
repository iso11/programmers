def solution(name):
    answer = 0

    # A아닌 알파벳 
    # ABCDEFGHIJKLM N OPQRSTUVWXYZ
    # print(ord('N') - ord('A'))
    # print(ord('Z') - ord('N') + 1) #ascii code!!

    count = []
    # 각 알파벳 count 구하기
    for i in range (0, len(name)):
        count.append(min(ord(name[i]) - ord('A'), (ord('Z') - ord(name[i]) + 1))) #ord : ascii code 구하기
    
    answer += sum(count)
    # 좌우 이동 구하기
    idx = 0
    while 1:
        left, right = 1, 1
        count[idx] = 0
        if sum(count) == 0:
            break
        while count[idx+right] == 0:
            right += 1
        while count[idx-left] == 0: # 인덱스가 마이너스면 맨 뒤로감
            left += 1
        if left < right:
            idx -= left
            answer += left
        else:
            idx += right
            answer += right

    return answer

print(solution("JAZ"))
print(solution("JEROEN"))
print(solution("JAN"))
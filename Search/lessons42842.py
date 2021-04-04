def solution(brown, yellow):
    answer = []

    # 두 개 더해서 총 갯수 구하고
    total = brown + yellow
    # 소인수분해
    for i in range(total//3, 2, -1): #i가 가로
        b, y = 0, 0
        if total%i == 0:
            b = i*2 + (total//i -2)*2 # 테두리 계산
            y = total - b # 가운데 계산
            if b == brown and y == yellow: # 일치하면 끝
                answer.append(i)
                answer.append(total//i)
                break

    return answer

print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))
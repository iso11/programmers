def solution(n, lost, reserve):
    answer = 0
    result = [1] * n

    # 갯수 list에 저장
    for i in range (n):
        if lost.count(i+1) > 0: # list.count(n) list리스트안에 n인 value가 몇개있는지
            result[i] -= 1
        if reserve.count(i+1) > 0:
            result[i] += 1
    
    # 2를 찾아서 앞뒤로 줄 수 있는지 확인
    for i in range (0, n):
        if result[i] == 2:
            if i-1 >= 0 and result[i-1] == 0:
                result[i-1] = 1
                result[i] = 1
            elif i+1 < n and result[i+1] == 0:
                result[i+1] = 1
                result[i] = 1

    answer = len(list(filter(lambda x: x >= 1, result))) # filter, lambda

    return answer

print(solution(5, [2,4], [1,3,5]))
print(solution(5, [2,4], [3]))
print(solution(3, [3], [1]))
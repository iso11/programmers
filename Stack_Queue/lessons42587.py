def solution(priorities, location):
    answer = 0

    #제일큰거 찾기
    #location이 제일 큰 값이면 종료
    #첫번째가 max 아니면 뒤로 보내기
    #첫번째가 제일클때 pop answer + 1
    #뒤로 보낼때 location이 0이 아니면 -1 0이면 제일 뒷번호로

    while priorities:
        maxIndex = priorities.index(max(priorities))
        if (maxIndex == location):
            return answer+1
        else:
            if maxIndex == 0:
                priorities.pop(0)
                answer += 1
            else:
                priorities.append(priorities.pop(0))
            if location == 0:
                location = len(priorities) - 1
            else:
                location -= 1

    return answer

print(solution([1, 1, 9, 1, 1, 1], 0))
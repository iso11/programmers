def solution(progresses, speeds):
    answer = []

    #(100 - progresses / speeds) + 1?? 로 남은 일 수 계산 후 큐에 담기
    #앞에꺼 빼면서 일수가 작으면 같이 빼기
    #빠진숫자 answer 배열에 추가
    days = []
    temp = 0;

    for i in range(0, len(progresses)):
        divResult = divmod((100 - progresses[i]), speeds[i])
        if (divResult[1] > 0):
            temp = divResult[0] + 1
        else:
            temp = divResult[0]
        days.append(temp)
    
    temp = 0
    while days:
        popt = days.pop(0)
        temp += 1
        while days and popt >= days[0]:
            temp += 1
            days.pop(0)
        answer.append(temp)
        temp = 0
    return answer
    


print(solution([95, 90, 99, 99, 80, 99]	, [1, 1, 1, 1, 1, 1]))
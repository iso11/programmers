def solution(answers):
    answer = []
    # 1
    soo1 = [1,2,3,4,5]
    #2
    soo2 = [2, 1, 2, 3, 2, 4, 2, 5]
    #3
    soo3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    count = [0,0,0]

    for i in range(0,len(answers)):
        if soo1[i%5] == answers[i]:
            count[0] += 1
        if soo2[i%8] == answers[i]:
            count[1] += 1
        if soo3[i%10] == answers[i]:
            count[2] += 1
    # count max값 찾아서 count랑 비교
    for i in range(len(count)):
        if count[i] == max(count):
            answer.append(i+1)
    answer.sort()

    #참고 - for문 index랑 값 같이 받아오기
    for i, a in enumerate(count):
        print(i, a)
            
    return answer

print(solution([1,2,3,4,5]))
# print(solution([1,3,2,4,2]))
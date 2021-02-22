def solution(prices):
    answer = []

    for i in range(0, len(prices)-1):
        time = 1
        for j in range(i+1, len(prices)-1):
            if (prices[i] > prices[j]): break
            else: time += 1
        answer.append(time)

    answer.append(0)
    return answer

print(solution([1, 2, 3, 2, 3]))
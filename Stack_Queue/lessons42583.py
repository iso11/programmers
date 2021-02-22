def solution(bridge_length, weight, truck_weights):
    answer = 0
    cTruck = [] #다리에 올라가있는 트럭
    cTime = [] #올라간 시점

    while (cTruck or truck_weights):
        answer += 1
        if (cTruck):
            if (answer-cTime[0] == bridge_length):
                cTruck.pop(0)
                cTime.pop(0)
        if (truck_weights):
            if (sum(cTruck) + truck_weights[0] <= weight):
                cTruck.append(truck_weights[0])
                cTime.append(answer)
                truck_weights.pop(0)

    return answer

# print(solution(2, 10, [7,4,5,6]))
print(solution(100, 100, [10]))
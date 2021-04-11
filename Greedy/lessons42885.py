def solution(people, limit):
    answer = 0
    people = sorted(people, reverse=True)

    #최대 두명
    # while people:
    #     if len(people) >= 2:
    #         if people[0] + people[-1] <= limit:
    #             people.pop(0)
    #             people.pop()
    #             answer += 1
    #         else:
    #             people.pop(0)
    #             answer += 1
    #     else:
    #         people.pop()
    #         answer += 1

    i,j = 0, len(people)-1
    while i <= j:
        answer += 1
        if people[i] + people[j] <= limit:
            i += 1
            j -= 1
        else:
            i +=1
            
    return answer

print(solution([70, 50, 80, 50], 100))
print(solution([50, 70, 80], 100))
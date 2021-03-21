def solution(operations):
    answer = []

    for op in operations:
        id = op.split()[0]
        number = int(op.split()[1])
        if id == "I":
            answer.append(number)
            answer.sort()
        elif len(answer) > 0:
            if number == 1:
                answer.pop()
            else:
                answer.pop(0)
    
    if len(answer) == 0:
        answer = [0, 0]
    else:
        answer = [max(answer), min(answer)]

    return answer

print(solution(	["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))
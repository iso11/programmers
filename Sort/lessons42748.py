def solution(array, commands):
    answer = []
    ar = array

    # for cm in commands:
    #     tmp = []
    #     for i in range(cm[0]-1, cm[1]):
    #         tmp.append(ar[i])
    #     tmp.sort()

    #     answer.append(tmp[cm[2]-1])

    for i,j,k in commands:
        answer.append(sorted(array[i-1:j])[k-1])

    return answer

print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))
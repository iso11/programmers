def solution(money):
    # 정답은 맞는데 효율성이 안나옴....
    # p_list = [money[0], money[1]]
    # p_list2 = [0, money[1]]
    #
    # for i in range(2, len(money)-1):
    #     p_list.append(max(p_list[:i-1]) + money[i])
    #
    # for i in range(2, len(money)):
    #     p_list2.append(max(p_list2[:i-1]) + money[i])

    p_list = [0] * len(money)
    p_list2 = [0] * len(money)
    p_list[0], p_list[1] = money[0], max(money[0], money[1])
    p_list2[1] = money[1]

    for i in range(2, len(money)-1):
        p_list[i] = max(p_list[i-2] + money[i], p_list[i-1])

    for i in range(2, len(money)):
        p_list2[i] = max(p_list2[i-2] + money[i], p_list2[i-1])

    return max(max(p_list), max(p_list2))

print(solution([1,2,3,1]), 4)
print(solution([1,1,4,1,4]), 8)
print(solution([1000,0,0,1000,0,0,1000,0,0,1000]), 3000)
print(solution([1000,1,0,1,2,1000,0]), 2001)
print(solution([1000,0,0,0,0,1000,0,0,0,0,0,1000]), 2000)
print(solution([1,2,3,4,5,6,7,8,9,10]), 30)
print(solution([0,0,0,0,100,0,0,100,0,0,1,1]), 201)
print(solution([11,0,2,5,100,100,85,1]), 198)
print(solution([1,2,3]), 3)
print(solution([91,90,5,7,5,7]), 104)
print(solution([90,0,0,95,1,1]), 185)

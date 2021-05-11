def solution(N, number):
    answer = -1
    p_set = []

    for i in range(1, 9):
        temp = set({int(str(N)*i)})

        for j in range(0, i-1):
            for k in p_set[j]:
                for m in p_set[-j-1]:
                    temp.add(k+m)
                    temp.add(k-m)
                    temp.add(k*m)
                    if m != 0:
                        temp.add(k//m)
        p_set.append(temp)

        if number in p_set[i-1]:
            answer = i
            break

    return answer
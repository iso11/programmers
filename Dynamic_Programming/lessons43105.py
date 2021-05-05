def solution(triangle):
    # https://galid1.tistory.com/507
    sum = [[triangle[0][0]]]

    for i, t in enumerate(triangle[1:]):
        temp = []
        for j, n in enumerate(t):
            if j == 0:
                temp.append(sum[i][0] + n)
            elif j == len(t) -1 :
                temp.append(sum[i][i] + n)
            else:
                temp.append(max(sum[i][j-1]+n, sum[i][j]+n))
        sum.append(temp)

    return max(sum[-1])

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
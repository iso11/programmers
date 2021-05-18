def solution(m, n, puddles):
    answer = 0

    #지도 그리기 0으로
    p_map = [[0 for i in range(0, m+1)] for j in range(n+1)]
    p_map[1][1] = 1

    #윗줄부터 합 구해가기
    for i in range(1, n+1):
        for j in range(1, m+1):
            if [j,i] not in puddles:
                p_map[i][j] += (p_map[i-1][j] + p_map[i][j-1])

    return p_map[n][m] % 1000000007

print(solution(4, 3, [[2,2]]))

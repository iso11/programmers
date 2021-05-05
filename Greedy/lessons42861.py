def solution(n, costs):
    costs.sort(key = lambda x: x[2]) # costs 순으로 정렬
    answer = costs[0][2]
    con = set([costs[0][0],costs[0][1]])
    i = 0

    #  모두 연결되었는지 확인해야함. -> 연결하면서 최소로.
    while len(con) != n:
        i = i + 1
        if costs[i][0] in con and costs[i][1] in con:
            continue
        if costs[i][0] in con or costs[i][1] in con:
            con.add(costs[i][0])
            con.add(costs[i][1])
            answer = answer + costs[i][2]
            i = 0

    return answer
# 4
# 3
# 6
# 15
# 6
# 9
# 4
# 14
# 11
# 14
# 8
print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))
print(solution(4,[[0,1,1],[0,2,1],[1,2,1],[1,3,1],[2,3,8]]))
print(solution(5,[[1,2,3],[0,1,1],[0,4,5],[2,4,1],[2,3,1],[3,4,1]]))
print(solution(5,[[0,1,5],[1,2,3],[2,3,3],[3,1,2],[3,0,4],[2,4,6],[4,0,7]]))
print(solution(5,[[0, 1, 1], [2, 3, 1], [3, 4, 2], [1, 2, 2], [0, 4, 100]]))
print(solution(4, [[0, 1, 5], [1, 2, 3], [2, 3, 3], [3, 1, 2], [3, 0, 4]]))
print(solution(4,[[0,1,1],[0,2,2],[2,3,1]]))
print(solution(7, [[1,0,1],[3,2,1],[4,5,1],[3,5,9],[3,6,10],[1,6,1],[6,5,1]]))
print(solution(6,[[0, 1, 5], [0, 3, 2], [0, 4, 3], [1, 4, 1], [3, 4, 10], [1, 2, 2], [2, 5, 3], [4, 5, 4]]))
print(solution(6, [[0,1,1],[3,1,1],[2,3,3],[2,4,4],[5,4,5]]))
print(solution(5,[[0,1,1],[3,4,1],[1,2,2],[2,3,4]]))
def solution(routes):
    answer = 0
    routes.sort(key = lambda x: x[0], reverse=True)

    point = routes[0][1] + 1

    for r in routes:
        if point > r[1]:
            point = r[0]
            answer += 1

    return answer

print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]]));
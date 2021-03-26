# H-index
def solution(citations):
    answer = 0
    
    citations.sort(reverse=True)
    print(citations)
    for i in range(0,len(citations)):
        if i < citations[i] :
            answer = i + 1
        i += 1
    
    return answer

print(solution([3, 0, 6, 1, 5]));
# print(solution([20,19,18,1]))
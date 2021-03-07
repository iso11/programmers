import heapq

#https://docs.python.org/ko/3.10/library/heapq.html
def solution(scoville, K):
    answer = 0
    heap = []

    for value in scoville:
        heapq.heappush(heap, value)

    while heap[0] < K:
        if len(heap) <= 1:
            answer = -1 
            break;
        heapq.heappush(heap, heapq.heappop(heap) + heapq.heappop(heap)*2)
        answer += 1

    return answer

print(solution([1, 2, 3, 9, 10, 12], 7))
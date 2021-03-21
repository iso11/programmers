import heapq

def solution(jobs):
    current = 0
    sum = 0
    wait = []
    count = 0
    end = -1
    
    while(count < len(jobs)):
        # wait에 들어갈 애들 넣어주기
        for job in jobs:
            if (end < job[0] <= current):
                heapq.heappush(wait, [job[1], job[0]])
        
        # 대기하는 애들이 있으면 처리
        if (wait):
            end = current
            current += wait[0][0]
            sum += (current - wait[0][1])
            heapq.heappop(wait) #heapq는 heappop으로 pop!
            count += 1
            
        # 없으면 현재시간 + 1
        else:
            current += 1

    return int(sum/count);

print(solution([[0, 3], [1, 9], [2, 6]]))
count = 0
def sum(level, s, numbers, target):
    global count
    if level == len(numbers):
        if s == target:
            count += 1
    else:
        sum(level+1, s+numbers[level], numbers, target)
        sum(level+1, s-numbers[level], numbers, target)

def solution(numbers, target):
    global count
    sum(0, 0, numbers, target)

    return count

print(solution([1, 1, 1, 1, 1], 3), 5)
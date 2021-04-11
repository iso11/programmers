def solution(number, k):
    answer = ''
    # k개 제거 할 수 있음
    # 들어있는게 작으면 빼기
    # n = list(number) #string list를 int list로

    while number:
        while answer and answer[-1] < number[0] and k > 0:
            answer = answer[:-1]
            k -= 1
        answer += number[0]
        number = number[1:]
        
    if k > 0:
        answer = answer[:-k]

    return answer

print(solution("1924", 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))
print(solution("999", 2))
print(solution("111119", 3))
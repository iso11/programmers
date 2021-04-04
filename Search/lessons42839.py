import itertools

def solution(numbers):
    # 조합 만들기 (리스트에 push)
    number = list(numbers) # 스트링을 리스트로
    totalList = []

    #python 순열, 조합 - https://medium.com/@hckcksrl/python-permutation-combination-a7bf9e5d6ab3 
    for i in range(1, len(number)+1):
        temp = list(map(''.join, itertools.permutations(number, i)))
        temp = [int (i) for i in temp] # string list 를 int list로 
        for t in temp:
            if t != 0 and t!= 1:
                flag = True
                for i in range(2, t//2+1):
                    if t%i == 0:
                        flag = False
                        break
                if flag:
                    totalList.append(t)
    
    totalList = list(set(totalList)) # list 중복제거 하는법: set으로 변경 후 다시 list로 

    return len(totalList)

print(solution("17"));
# print(solution("011"));
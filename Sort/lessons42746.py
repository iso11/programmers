def solution(numbers):
    answer = ''
    strList = list(map(str, numbers)) #number 리스트를 string 리스트로
    strList.sort(key = lambda x: x*3, reverse=True) #https://free-eunb.tistory.com/71 sort할때 조건주기

    return str(int(''.join(strList))) #0 방어

print(solution([3, 30, 34, 5, 9]))
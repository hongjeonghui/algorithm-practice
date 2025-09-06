def solution(n):
    answer = 0
    n = str(n)  # 숫자는 하나씩 뽑지 못하니까 문자열로 전환
    for i in n:
        answer += int(i)  # 다시 정수형으로 변환
    
    return answer

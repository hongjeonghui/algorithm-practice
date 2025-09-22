# 내 풀이
def solution(my_string):
    answer = []
    for i in my_string:
        if i in ['1','2','3','4','5','6','7','8','9','0']:
            answer.append(int(i))
    answer.sort()
    return answer

# 메서드를 사용한 풀이 (리스트 컴프리헨션 + isdigit())
def solution(my_string):
    return sorted([int(c) for c in my_string if c.isdigit()])

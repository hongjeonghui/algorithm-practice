def solution(sides):
    a, b = sides
    mx = max(a, b)
    mn = min(a, b)
    
    # x가 가장 긴 변
    case1 = (a + b - 1) - mx + 1
    
    #  x가 가장 긴 변이 아님
    case2 = (mx - 1) - (mx - mn + 1) + 1
    
    return case1 + case2

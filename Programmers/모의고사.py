def solution(answers):
    # 1번, 2번, 3번 루틴
    num1 = [1, 2, 3, 4, 5]
    num2 = [2, 1, 2, 3, 2, 4, 2, 5]
    num3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    score1, score2, score3 = 0, 0, 0
    
    for i, answer in enumerate(answers):
        if answer == num1[i % len(num1)]:
            score1 += 1
        if answer == num2[i % len(num2)]:
            score2 += 1
        if answer == num3[i % len(num3)]:
            score3 += 1
            
    max_score = max(score1, score2, score3)
    
    result = []
    if score1 == max_score:
        result.append(1)
    if score2 == max_score:
        result.append(2)
    if score3 == max_score:
        result.append(3)
        
        
    return result

def solution(array, n):
    answer = []
    num = ''
    array.sort(reverse=True)
    for i in array:
        answer.append(abs(i-n))
    for i, k in enumerate(answer):
        if min(answer) == k:
            num = i
    return array[num]

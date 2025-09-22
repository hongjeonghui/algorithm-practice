def solution(cipher, code):
    answer = ''  # 결과 문자열을 담을 변수

    # 시작: code-1 → 사람이 생각하는 code번째 글자의 인덱스
    for i in range(code-1, len(cipher), code):
        answer += cipher[i]  # 해당 위치 문자를 answer에 이어붙이기

    return answer  # 완성된 문자열 반환

def solution(a, b):
    import datetime
    date = datetime.date(2016, a, b)
    answer = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    return answer[date.weekday()]

def solution(numbers):
    word_to_num = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }

    result = ""
    temp = ""

    for ch in numbers:
        temp += ch
        if temp in word_to_num:
            result += word_to_num[temp]
            temp = ""

    return int(result)

# https://school.programmers.co.kr/learn/courses/30/lessons/120836

def solution(n):
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            count += 1
            if n // i != i: 
                count += 1
    return count

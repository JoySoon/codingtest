# https://school.programmers.co.kr/learn/courses/30/lessons/120835

def solution(emergency):
    
    sorted_ = sorted(range(len(emergency)), key=lambda x: emergency[x])
    
    order_ = [len(emergency) - sorted_.index(i) for i in range(len(emergency))]

    return order_
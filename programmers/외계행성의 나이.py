# https://school.programmers.co.kr/learn/courses/30/lessons/120834

def solution(age):
    alphabet_order = "abcdefghijklmnopqrstuvwxyz"
    age_in_alphabet = ""
    
    while age > 0:
        age, remainder = divmod(age, 10)
        age_in_alphabet = alphabet_order[remainder] + age_in_alphabet

    return age_in_alphabet
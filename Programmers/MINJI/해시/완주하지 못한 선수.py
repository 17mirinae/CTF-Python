def solution(participant, completion):
    answer = ''
    
    for name in participant:
        if name not in completion:
            answer = name
            break

    return answer

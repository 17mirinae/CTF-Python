def solution(participant, completion):
    answer = ''
    
    for name in participant:
        if name not in completion:
            answer = name
            break

    return answer

# 다른 사람 코드
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
# collections.Counter

from collections import Counter
from functools import reduce
from operator import mul

def solution(clothes):
    return reduce(mul, [cnt + 1 for cnt in Counter([cat for _, cat in clothes]).values()]) - 1

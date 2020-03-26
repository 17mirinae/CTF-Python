#!/usr/bin/env python2
# coding: utf-8

import time
import random
import operator
from pwn import *

def get_random():
    return random.randint(1, 5000) * 2



def main():
    test_time = 1000
    p = process('./5.골드바흐의추측.py')
    p.sendline(str(test_time))

    tested = {}
    for _ in range(test_time):
        test = get_random()
        print("Testing {0} ... ".format(test), end="")
        before = time.time()

        p.sendline(str(test))
        res = p.recvline().strip()

        after = time.time()
        execute_time = after - before
        # tested.append({test: execute_time})
        tested[test] = execute_time

        print("{0}s".format(execute_time))
        print(res)


    long_exec = max(tested, key=tested.get)
    print("[*] the longgest item :", long_exec)
    print(" └━ time :", tested[long_exec])


    times = [exec_time for _, exec_time in tested.items()]
    print("[*] average time : {0}s".format(sum(times) / len(times)))



if __name__ == '__main__':
    main()

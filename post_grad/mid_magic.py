'''
given a non negative digit k, find the balanced n such that
sum between 1 to n equals sum between n to k

input k = 49
output = 35
explanation: sum of numbers from 1-35 == sum of numbers from 35-49

if non: return -1
'''

from time import time


def solution(k: int) -> int:
    '''return magic number'''

    for i in range(k):
        if (sum(range(1, i + 1)) == sum(range(i, k + 1))):
            return i
    return -1


def optimized(k):

    n = sum(range(k + 1))
    i_sum = 0

    for i in range(k):
        if (i_sum == n - (i_sum - i)):
            return i
        i_sum += i + 1
    return - 1


start = time()
# Test
print(solution(288))

end = time()
print('solution time =', end - start)

start = time()
# Test
print(optimized(288))

end = time()
print('optimized time =', end - start)

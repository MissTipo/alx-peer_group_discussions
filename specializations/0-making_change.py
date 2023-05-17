#!/usr/bin/python3
"""
coins = [1, 2, 25]
total = 37
sort = [25, 2, 1]
counter, total
0, 37
1, 12
2, 10
3, 8
4, 6
5, 4
6, 2
7, 0
25
new_total = 37 - 25 = 12
1 = 12 coins
2 = 6
(1, 2)
coins = [1256, 54, 48, 16, 102]
total = 1453
sort = [1256, 102, 54, 48, 16]

counter, total
0, 1453
1, 197
2, 95
3, 41
4, 25
5, 9




1453 - 1256 = 197
197 - 102 = 95
95 - 54 = 41
41 - 16 = 25
25 - 16 = 9


if sum(coins) = total:
    return len(coins)

sorted_coins = sorted(coins, reverse=True)
for i in range(len(coins)):
    if sorted_coins[i] = total:
        return sorted_coins[i]
if min(coins) > total:
    return -1

"""

def makeChange(coins, total):
    """"""
    counter = 0
    if total <= 0:
        return 0
    if min(coins) > total:
        return -1
    if sum(coins) == total:
        return len(coins)
    if total in coins:
        return 1
    sort = sorted(coins, reverse=True)
    for i in range(len(sort)):
        while sort[i] <= total:
            total = total - sort[i]
            counter += 1
    if total == 0:
        return counter
    return -1

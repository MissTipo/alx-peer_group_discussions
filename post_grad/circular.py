'''
Jogging Track distance

imagine a circular track with several rest points from 0 to n - 1.
The distance between each rest point is known and recorded in an array called distance[i]
where distance[i] shows the distance between point i and point(i + 1) % n.
A person wants to find the minimum distance between two chosen rest points, starts and destination
on the circular route, while being able to travel in both directions, clockwise and counterclockwise

input: distance = [1, 2, 3, 4], start = 0, destination = 1
output =: 1
explanation: Distance between 0 and 1 is 1 and 9, minimum is 1.
'''


def solution(distance: list[int], start: int, dest: int) -> int:

    f = 0

    for i in range(start, dest):
        f += distance[i]

    b = sum(distance) - f

    return min(f, b)


distance = [1, 2, 3, 4]
s = 0
d = 2

print(solution(distance, s, d))

'''
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104

pseudocode:
    if target is greater than matrix[-1][-1] or target is less than matrix[0][0]:
        return False
    
    for i in range(len(matrix)):
        if target is <= matrix[i][-1]:
            if target == matrix[i][-1]:
                return True

            # Start binary search for matrix[i]
            # get length of matrix[i] and divide by 2
            # Check value at mid section
            # check right and left for available spot

            mid = len(matrix(i)) // 2
            if target == matrix[i][mid]:
                return true
            start = 0
            end = 0

            if target < matrix[i][mid]:

                
        # Binary search Algorithm
        b_search(arr, target, start:0, end:l):  # [1,2,3,4,5,6,7,8,9] target = 2
            mid = end // 2    mid = 4: 
            if arr[mid] == target:
                return True

            if target < arr[mid]:  # if 2 < 5
                # search left       # new array = [1,2,3,4]
                start = start
                end = mid - 1
                b_search(arr, target, start, end)

            else:
                start = mid + 1
                b_search(arr, target, start, end)
            

'''


def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    if target > matrix[-1][-1] or target < matrix[0][0]:
        return False

    for i in range(len(matrix)):
        if target <= matrix[i][-1]:
            if target == matrix[i][-1]:
                return True

            return binary_search(matrix[i], target)
    return False


def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return True  # Target found, return its index
        elif arr[mid] < target:
            left = mid + 1  # Target is in the right half
        else:
            right = mid - 1  # Target is in the left half

    return False  # Target is not in the array


matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 13

print('Testing123')
print(searchMatrix(matrix, target))


# for i in range(10):
# print(binary_search(arr, i))

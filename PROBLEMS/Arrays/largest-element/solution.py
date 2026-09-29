import math

from dsa import run

'''
Given an array of integers nums, return the value of the 
largest element in the array
'''

class Solution:

    def solve(self, nums):
        largest = -math.inf
        for num in nums:
            if num > largest:
                largest = num
        return largest


if __name__ == '__main__':
    run(Solution().solve)

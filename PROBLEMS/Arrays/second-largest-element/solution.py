import math

from dsa import run

'''
Given an array of integers nums, return the second-largest 
element in the array. If the second-largest element does not
exist, return -1.
[8, 8, 7, 6, 5]

'''

class Solution:

    def solve(self, nums):
        largest =  -math.inf
        secLarget = -math.inf

        for num in nums:
            if num > largest:
                secLarget = largest
                largest = num
            elif num > secLarget and num!= largest:
                secLarget = num
        if secLarget == -math.inf:
            return -1
        else:
            return secLarget


if __name__ == '__main__':
    run(Solution().solve)

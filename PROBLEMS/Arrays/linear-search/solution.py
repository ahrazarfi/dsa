from dsa import run

'''
Given an array of integers nums and an integer target, 
find the smallest index (0 based indexing) where the
target appears in the array. If the target is not 
found in the array, return -1
'''

class Solution:

    def solve(self, nums, target):
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1


if __name__ == '__main__':
    run(Solution().solve)

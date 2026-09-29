from dsa import run

'''
Given an integer array nums, rotate the array to the left by one.

Note: There is no need to return anything, just modify the given array.

1 <= nums.length <= 105
-104 <= nums[i] <= 104

Input: nums = [1, 2, 3, 4, 5]

Output: [2, 3, 4, 5, 1]

Explanation:

Initially, nums = [1, 2, 3, 4, 5]

Rotating once to left -> nums = [2, 3, 4, 5, 1]

'''

class Solution:

    def solve(self, nums):
        # extract the first element
        first = nums[0]
        # traverse from 1 to len(nums)
        for i in range(1,len(nums)):
            nums[i-1] = nums[i]
        nums[-1] = first


if __name__ == '__main__':
    run(Solution().solve, in_place=True)

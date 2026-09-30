from dsa import run

'''
Given an integer array nums, move all the 0's to the end of the array. The relative order of the 
other elements must remain the same.

This must be done in place, without making a copy of the array.

Given an integer array nums, move all the 0's to the end of the array. The relative order of the 
other elements must remain the same.

This must be done in place, without making a copy of the array.

Example 1:
Input: nums = [0, 1, 4, 0, 5, 2]

Output: [1, 4, 5, 2, 0, 0]

Explanation:

Both the zeroes are moved to the end and the order of the other elements stay the same

'''

class Solution:

    def solve(self, nums):
        # read = 0
        written = 0

        # for i in range(len(nums)):
        #     read += 1
        #     if nums[i] != 0:
        #         nums[written] = nums[i]
        #         written += 1
        # for i in range(written, len(nums)):
        #     nums[i] = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[written], nums[i] = nums[i], nums[written]
                written += 1


if __name__ == '__main__':
    # input.txt: one value per line, one line per argument; blank line between test cases
    # expected.txt (optional): one value per case. Options for run():
    #   in_place=True   unordered=True   tol=1e-5   check=fn(args, out)   parse=[to_linked, to_tree, None]
    run(Solution().solve, in_place=True)

from dsa import run

'''
Given an integer array nums and a non-negative integer k, rotate the array to the left by k steps.

Example 1:
Input: nums = [1, 2, 3, 4, 5, 6], k = 2
[2,1,3,4,5,6], [2,1,6,5,4,3], [3,4,5,6,1,2]
Output: nums = [3, 4, 5, 6, 1, 2]

Explanation:

rotate 1 step to the left: [2, 3, 4, 5, 6, 1]

rotate 2 steps to the left: [3, 4, 5, 6, 1, 2]
'''

class Solution:

    def solve(self, nums, k):
        # the intuition is that after len(nums) rotations the array will come back to its orig form
        # so we need to find effective rotations 
        k = k % len(nums)

        start = 0
        stop = k-1

        while start < stop:
            nums[start], nums[stop] = nums[stop], nums[start]
            start += 1
            stop -= 1

        start = k
        stop = len(nums) -1

        while start < stop:
            nums[start], nums[stop] = nums[stop], nums[start]
            start += 1
            stop -= 1

        start = 0
        stop = len(nums) -1

        while start < stop:
            nums[start], nums[stop] = nums[stop], nums[start]
            start += 1
            stop -= 1



if __name__ == '__main__':
    # input.txt: one value per line, one line per argument; blank line between test cases
    # expected.txt (optional): one value per case. Options for run():
    #   in_place=True   unordered=True   tol=1e-5   check=fn(args, out)   parse=[to_linked, to_tree, None]
    run(Solution().solve, in_place=True)

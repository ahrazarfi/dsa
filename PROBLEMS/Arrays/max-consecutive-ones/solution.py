from dsa import run

'''
Given a binary array nums, return the maximum 
number of consecutive 1s in the array.
A binary array is an array that contains only 0s and 1s.


Input: nums = [1, 1, 0, 0, 1, 1, 1, 0]

Output: 3
'''

class Solution:

    def solve(self, nums):
        count = 0
        ans = 0
        for num in nums:
            if num == 1:
                count += 1
                ans = max(count, ans)
            else:
                count = 0
        return ans


if __name__ == '__main__':
    run(Solution().solve)

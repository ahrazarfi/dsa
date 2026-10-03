from dsa import run
'''
Given an integer array nums, return a list of all the leaders in the array.

A leader in an array is an element whose value is strictly greater than all elements to its right in the given array. The rightmost element is always a leader. The elements in the leader array must appear in the order they appear in the nums array.

Example 1:
Input: nums = [1, 2, 5, 3, 1, 2]

Output: [5, 3, 2]

Explanation:

2 is the rightmost element, 3 is the largest element in the index range [3, 5], 5 is the largest element in the index range [2, 5]
'''

class Solution:

    def solve(self, nums):
        n =len(nums)
        max_right = nums[n-1]
        result = [max_right]
        for i in range(n-2, -1, -1):
            if nums[i] > max_right:
                max_right = nums[i]
                result.append(max_right)
        return result[-1::-1]


if __name__ == '__main__':
    # input.txt: one value per line, one line per argument; blank line between test cases
    # expected.txt (optional): one value per case. Options for run():
    #   in_place=True   unordered=True   tol=1e-5   check=fn(args, out)   parse=[to_linked, to_tree, None]
    run(Solution().solve)

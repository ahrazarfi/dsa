import ast
import os
import sys

here = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(os.path.join(here, 'input.txt'), 'r')
sys.stdout = open(os.path.join(here, 'output.txt'), 'w')

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
    # input.txt: one Python literal per line, one line per argument
    args = [ast.literal_eval(line) for line in sys.stdin if line.strip()]
    out = Solution().solve(*args)
    if out is None:  # in-place problem: show the modified first argument
        out = args[0]
    print(*out) if isinstance(out, list) else print(out)

import ast
import os
import sys

here = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(os.path.join(here, 'input.txt'), 'r')
sys.stdout = open(os.path.join(here, 'output.txt'), 'w')


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
    # input.txt: one Python literal per line, one line per argument
    args = [ast.literal_eval(line) for line in sys.stdin if line.strip()]
    out = Solution().solve(*args)
    if out is None:  # in-place problem: show the modified first argument
        out = args[0]
    print(*out) if isinstance(out, list) else print(out)

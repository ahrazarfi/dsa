import ast
import os
import sys
import math

here = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(os.path.join(here, 'input.txt'), 'r')
sys.stdout = open(os.path.join(here, 'output.txt'), 'w')

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
    # input.txt: one Python literal per line, one line per argument
    args = [ast.literal_eval(line) for line in sys.stdin if line.strip()]
    out = Solution().solve(*args)
    if out is None:  # in-place problem: show the modified first argument
        out = args[0]
    print(*out) if isinstance(out, list) else print(out)

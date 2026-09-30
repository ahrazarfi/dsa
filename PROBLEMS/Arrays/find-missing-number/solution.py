from dsa import run

'''
Given an integer array of size n containing distinct values in the range
from 0 to n (inclusive), return the only number missing from the array within this range.


Example 1:
Input: nums = [0, 2, 3, 1, 4]

Output: 5

Explanation:

nums contains 0, 1, 2, 3, 4 thus leaving 5 as the only missing number in the range [0, 5]
'''

class Solution:

    def solve(self, nums):
        n = len(nums)
        sum1 = 0
        for i in range(n+1):
            sum1 += i
        sum2 = sum(nums)
        return sum1-sum2



if __name__ == '__main__':
    # input.txt: one value per line, one line per argument; blank line between test cases
    # expected.txt (optional): one value per case. Options for run():
    #   in_place=True   unordered=True   tol=1e-5   check=fn(args, out)   parse=[to_linked, to_tree, None]
    run(Solution().solve)

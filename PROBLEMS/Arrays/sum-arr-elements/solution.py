import ast
import os
import sys

here = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(os.path.join(here, 'input.txt'), 'r')
sys.stdout = open(os.path.join(here, 'output.txt'), 'w')


class Solution:

    def solve(self, nums, n):
        total= 0
        for i in range(n):
            total += nums[i]
        return total
        
        


if __name__ == '__main__':
    # input.txt: one Python literal per line, one line per argument
    args = [ast.literal_eval(line) for line in sys.stdin if line.strip()]
    out = Solution().solve(*args)
    if out is None:  # in-place problem: show the modified first argument
        out = args[0]
    print(*out) if isinstance(out, list) else print(out)

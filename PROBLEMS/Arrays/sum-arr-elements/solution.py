from dsa import run

class Solution:

    def solve(self, nums, n):
        total= 0
        for i in range(n):
            total += nums[i]
        return total


if __name__ == '__main__':
    run(Solution().solve)

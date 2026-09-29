from dsa import run

class Solution:

    def solve(self, nums, n):
        count = 0
        for i in range(n):
            if nums[i] % 2 != 0:
                count += 1
        return count


if __name__ == '__main__':
    run(Solution().solve)

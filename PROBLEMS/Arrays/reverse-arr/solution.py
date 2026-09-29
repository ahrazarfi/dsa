from dsa import run

class Solution:

    def solve(self, arr, n):
        right = n-1
        left = 0
        while left < right:
            arr[right], arr[left] = arr[left], arr[right]
            left += 1
            right -= 1


if __name__ == '__main__':
    run(Solution().solve, in_place=True)

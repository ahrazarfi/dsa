from dsa import run

class Solution:

    def solve(self, arr, n):
        for i in range(n-1):
            if arr[i] > arr[i+1]:
                return False
        return True


if __name__ == '__main__':
    run(Solution().solve)

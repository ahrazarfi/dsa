from dsa import run

'''
Given an integer array nums of size n, return the majority element of the array.

The majority element of an array is an element that appears more than n/2 times in the array. The array is guaranteed to have a majority element.

Example 1:
Input: nums = [7, 0, 0, 1, 7, 7, 2, 7, 7]

Output: 7

Explanation:

The number 7 appears 5 times in the 9 sized array

Example 2:
'''

class Solution:

    def solve(self, nums):
        # using boyers moore voting algo

        count = 0
        candidate = nums[0]
        for i in range(len(nums)):
            if count == 0:
                candidate = nums[i]
                count += 1
            elif nums[i] == candidate:
                count +=1
            else:
                count -= 1
        return candidate



if __name__ == '__main__':
    # input.txt: one value per line, one line per argument; blank line between test cases
    # expected.txt (optional): one value per case. Options for run():
    #   in_place=True   unordered=True   tol=1e-5   check=fn(args, out)   parse=[to_linked, to_tree, None]
    run(Solution().solve)

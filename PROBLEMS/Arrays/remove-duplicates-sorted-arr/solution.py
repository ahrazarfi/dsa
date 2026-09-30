from dsa import run
import math

'''

Given an integer array nums sorted in non-decreasing order, remove all duplicates in-place so that 
each unique element appears only once.

Return the number of unique elements in the array.

If the number of unique elements be k, then,

Change the array nums such that the first k elements of nums contain the unique values in the 
order that they were present originally.
The remaining elements, as well as the size of the array does not matter in terms of correctness.
The driver code will assess correctness by printing and checking only the first k elements of the 
modified array.
An array sorted in non-decreasing order is an array where every element to the right of an element
is either equal to or greater in value than that element.

Example 1:
Input: nums = [0, 0, 3, 3, 5, 6]

Output: 4

Explanation:

Resulting array = [0, 3, 5, 6, _, _]

There are 4 distinct elements in nums and the elements marked as _ can have any value.
'''

class Solution:

    # count= 0
    def solve(self, nums):
        # init a variable which will be for unique elements, set idx 0 as unique initially
        seen = 0
        # we will use another pointer which will iterate over the arr, check if a unique element is found
        for i in range(1, len(nums)):
            # unique element found
            if nums[seen] != nums[i]:
                # position of unique element will be seen +1
                seen += 1
                nums[seen] = nums[i]
                # this way seen will be at the boundary of unique elements in the arr
        return nums[:seen+1]
        





if __name__ == '__main__':
    # input.txt: one value per line, one line per argument; blank line between test cases
    # expected.txt (optional): one value per case. Options for run():
    #   in_place=True   unordered=True   tol=1e-5   check=fn(args, out)   parse=[to_linked, to_tree, None]
    run(Solution().solve)

from dsa import run

'''
Given two sorted arrays nums1 and nums2, return an array that contains the union of these two arrays. 
The elements in the union must be in ascending order.

The union of two arrays is an array where all values are distinct and are present in either the first array, 
the second array, or both.

Example 1:
Input: nums1 = [1, 2, 3, 4, 5], nums2 = [1, 2, 7]

Output: [1, 2, 3, 4, 5, 7]

Explanation:

The elements 1, 2 are common to both, 3, 4, 5 are from nums1 and 7 is from nums2

'''

class Solution:

    def solve(self, nums1, nums2):
        # two pointers one for each arr
        i, j = 0, 0

        result = []    
        # loop from 0 to len
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                if not result or result[-1] != nums1[i]:
                    result.append(nums1[i])
                i+=1
            elif nums1[i] > nums2[j]:
                if not result or result[-1] != nums2[j]:
                    result.append(nums2[j])
                j += 1
            else:
                if not result or result[-1] != nums1[i]:
                    result.append(nums1[i])
                i += 1
                j += 1
        while i < len(nums1):
            if not result or result[-1] != nums1[i]:
                result.append(nums1[i])
            i += 1

        while j < len(nums2):
            if not result or result[-1] != nums2[j]:
                result.append(nums2[j])     
            j +=1
        return result   
        


if __name__ == '__main__':
    # input.txt: one value per line, one line per argument; blank line between test cases
    # expected.txt (optional): one value per case. Options for run():
    #   in_place=True   unordered=True   tol=1e-5   check=fn(args, out)   parse=[to_linked, to_tree, None]
    run(Solution().solve)

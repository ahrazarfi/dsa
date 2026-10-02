from dsa import run


class Solution:
    def solve(self, nums1, nums2):
        # using two pointers

        i,j = 0,0

        result = []
        while i < len(nums1) and j < len(nums2):
            # first case where insertion happens
            if nums1[i] == nums2[j]:
                result.append(nums1[i])
            
                i += 1
                j += 1
            # second case is when nums1 < nums2

            elif nums1[i] < nums2[j]:
                # becasue arrays are sorted we know
                # that anything equal will be found further ahead in nums1

                i += 1
            else:
                j += 1
        return result



if __name__ == '__main__':
    # input.txt: one value per line, one line per argument; blank line between test cases
    # expected.txt (optional): one value per case. Options for run():
    #   in_place=True   unordered=True   tol=1e-5   check=fn(args, out)   parse=[to_linked, to_tree, None]
    run(Solution().solve)

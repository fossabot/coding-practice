# What if the given array is already sorted? How would you optimize your algorithm?
# What if nums1's size is small compared to nums2's size? Which algorithm is better?
# What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?


from typing import List


class Solution:

    @classmethod
    def intersect(cls, nums1: List[int], nums2: List[int]) -> List[int]:

        intersection = []
        
        # Solution 1: O(n) time, O(n) space
        # search for as few elements as possible
        for element in nums1:
            if element in nums2:
                intersection.append(element)
                nums2.remove(element)
                            
        # # Solution 2: O(n) time, O(n) space
        # # if the arrays are sorted, I can start searching for
        # # common elements at the smallest item in nums2 that is in nums1
        
        # i = 0
        # # find the first item in nums1 that could be in nums2
        # while i < len(nums1):
        #     if nums1[i] >= nums2[0]:
        #         print("Found num[{}] = {}, breaking".format(i, nums1[i]))
        #         break
        #     i += 1

        # # now search for a correspondent in nums2
        # while i < len(nums1):
        #     if nums1[i] in nums2:
        #         intersection.append(nums1[i])
        #     i += 1
               
        # Solution 3: second array read from disk, one per line, output to disk
        # O(n) time, O(n) space
        # with open("intersection.txt", "a") as f:
        #     with open("/Users/inwaves/inwaves-repository/coding-practice/leetcode/arrays/nums2.txt", "r") as g:
        #         for line in g:
        #             if int(line.strip()) in nums1:
        #                 f.write(line.strip()  + "\n")

        return intersection


if __name__ == "__main__":

    print(Solution.intersect([1,2,2,1], [2]))
    # print(Solution.intersect([1, 2, 3, 4], [3, 4, 5]))

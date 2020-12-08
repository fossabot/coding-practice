# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

from typing import List


class Solution:
    @classmethod
    def moveZeroes(cls, nums: List[int]) -> List[int]:
        """
        Do not return anything, modify nums in-place instead.
        """

        if len(nums) == 0:
            return nums
        
        # # # go through each element, if it's a 0, remove it and increment a counter
        # # # add zeroes to the end
        # # # O(n) time, O(n) space
        # doesn't work, it changes the list size while iterating so it errors!
        # counter = 0
        # for i in range(len(nums)-1):
        #     if nums[i] == 0:
        #         print("Removed {}".format(nums[i]))
        #         nums.remove(nums[i])
        #         print("nums= {}, new_length = {}".format(nums, len(nums)))
        #         counter += 1
        #     print("Considered {}".format(nums[i]))
        # nums += [0] * counter

        # python nums.count(0), remove them, add them back
        # O(n) time—though depends on what .remove does; O(n) space
        count_zeroes = nums.count(0)
        while 0 in nums:
            nums.remove(0)
        nums += [0] * count_zeroes

        # # recursively: moveZeroes ([0 1 0 3 13]) = moveZeroes[1 0 3 13].append(0) = moveZeroes [0 3 13].insert(1).append(0) =
        # # = moveZeroes [3 13].insert(1).append(0).append(0)
        # # if it's a zero, append it to the result
        # # if it's nonzero, insert it at the front
        # O(n) time, O(n) space
        # if len(nums) == 1:
        #     return nums
        
        # nums = Solution.moveZeroes(nums[1:]) + [nums[0]] if nums[0] == 0 else [nums[0]] + Solution.moveZeroes(nums[1:])
        
        return nums


if __name__ == "__main__":

    tests = [[0],
             [0, 1, 0, 3, 13],
             [0, 0, 0, 1],
             [1, 0, 0, 0],
             [1, 2, 3, 4],
             []]

    for test in tests:
        print("in = {}, out = {}".format(test, Solution.moveZeroes(test)))
    # print(Solution.moveZeroes([0, 0, 1]))
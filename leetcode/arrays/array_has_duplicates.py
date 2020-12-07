from typing import List


class Solution:

    @classmethod
    def containsDuplicate(cls, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)

    @classmethod
    def containsDuplicateTwo(cls, nums: List[int]) -> bool:
        for item in nums:
            if nums.count(item) > 1:
                return True
        return False

    @classmethod
    def containsDuplicateThree(cls, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == nums[i+1]:
                return True
        return False

if __name__ == "__main__":

    print(Solution.containsDuplicate([6, 6, 3, 1, 1, 3, 4, 2]))
    print(Solution.containsDuplicateTwo([6, 6, 3, 1, 1, 3, 4, 2]))
    print(Solution.containsDuplicateThree([6, 6, 3, 1, 1, 3, 4, 2]))

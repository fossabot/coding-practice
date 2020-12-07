from typing import List

# sorted array, remove duplicates in place, return length

class Solution:
    
    @classmethod
    def removeDuplicates(cls, nums: List[int]) -> int:
        
        if list(set(nums)) != nums:
            for item in nums:
                while nums.count(item) > 1:
                    nums.remove(item)
                    
        return len(nums)
    
if __name__ == "__main__":
    mylist = [-1, 0, 0, 0, 0, 3, 3]
    print("Length: {}".format(Solution.removeDuplicates(mylist)))
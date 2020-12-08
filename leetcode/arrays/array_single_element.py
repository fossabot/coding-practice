from typing import List
from collections import defaultdict

# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# Implement a solution O(n) time, in-place?

class Solution:
    
    @classmethod
    def singleNumber(cls, nums: List[int]) -> int:

        # trivial
        # for example in nums:
        #     if nums.count(example) == 1:
        #         return example
        
        # using XOR since duplicates cancel out
        # a = 0
        # for i in nums:
        #     a ^= i
        # return a
        
        # maths: 2(a+b+c) - (a + a + b + b + c) = c
        # return 2 * sum(set(nums)) - sum(nums)
        
        # HashSet
        hash_table = defaultdict(int)
        for i in nums:
            hash_table[i] += 1
        
        for i in hash_table:
            if hash_table[i] == 1:
                return i
            
if __name__ == "__main__":
    
    print(Solution.singleNumber([2, 2, 1]))
    print(Solution.singleNumber([1, 1, 2]))
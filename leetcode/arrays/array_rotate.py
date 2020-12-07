from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start, end = nums[len(nums)-k:], nums[:len(nums)-k]
        start.extend(end)
        nums = start
        # print(nums)
        return nums
        
        
if __name__ == "__main__":
    
    test_cases = [[[1, 2, 3, 4], 1],
                  [[6, 31, 3, 92, 7], 3], 
                  [[1,2,3,4,5,6,7],3]]
    
    results = [[4, 1, 2, 3],
               [3, 92, 7, 6, 31], 
               [5,6,7,1,2,3,4]]
    
    for test, result in zip(test_cases, results):
        mysol = Solution()
        print("Test: {} = {}".format(mysol.rotate(test[0], test[1]),result))
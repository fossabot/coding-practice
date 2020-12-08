# Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.
# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.
# You may assume the integer does not contain any leading zero, except the number 0 itself.


from typing import List


class Solution:
    @classmethod
    def plusOne(cls, digits: List[int]) -> List[int]:
        
        # # recursive
        # # O(n) time, O(1)? space?
        # if len(digits) == 1 and digits[0] == 9:
        #     return [1, 0]
        
        # if digits[-1] != 9:
        #     digits[-1] += 1
            
        # else:
        #     digits = Solution.plusOne(digits[:-1])
        #     digits.append(0)
            
        
        carry = 1
        i = len(digits)-1
        while carry != 0:
            if digits[i] == 9:
                digits[i] = 0
                if i == 0:
                    digits.insert(0, 1)
                    carry = 0
            else:
                digits[i] += carry
                carry = 0
            i -= 1
                
        return digits


if __name__ == "__main__":
    inputs = [[1, 2, 3], [1, 2, 9], [1, 9, 9], [3], [9]]
    for test in inputs:
        print("in = {}, out = {}".format(test, Solution.plusOne(test)))

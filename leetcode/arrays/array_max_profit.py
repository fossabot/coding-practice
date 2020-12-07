from typing import List


class Solution:

    @classmethod
    def maxProfit(cls, prices: List[int]) -> int:

        running_profit = 0
        for i in range(len(prices)-1):
            if prices[i+1] > prices[i]:
                running_profit += prices[i+1] - prices[i]

        return running_profit


if __name__ == "__main__":

    inputs = [[6, 1, 3, 2, 4, 7], [7, 1, 5, 3, 6, 4],
              [1, 2, 3, 4, 5], [7, 6, 4, 3, 1]]
    results = [7, 7, 4, 0]

    print(Solution.maxProfit(inputs[0]))
    
    for input, result in zip(inputs, results):
        print("Test: {} = {}".format(input, result))
        assert Solution.maxProfit(input) == result

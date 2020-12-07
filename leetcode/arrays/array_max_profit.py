from typing import List


class Solution:

    @classmethod
    def maxProfit(cls, prices: List[int]) -> int:

        profits = []
        for i in range(len(prices)-1):
            j = i + 1
            while j < len(prices):
                # traverse the array of prices

                # discount large prices the further away in the
                # future they are, since I would rather make a profit now
                if prices[j] > prices[i]:
                    profit = (prices[j] - prices[i]) / (j-i) if j-i > 2 else prices[j] - prices[i]
                    profits.append([i, j, profit])
                    print("i = {}\tj = {}\tprofit = {}".format(i, j, profit))
                j += 1

        profits.sort(reverse=True, key=lambda entry: entry[2])
        print("Profits: {}".format(profits))

        running_profit = 0
        highest_previous_sell = -1

        # calculate the max profit
        for i, j, profit in profits:
            if i > highest_previous_sell:
                highest_previous_sell = j
                running_profit += profit
                print("Added i={}, j={} p={}".format(i, j, profit))

        return running_profit


if __name__ == "__main__":

    inputs = [[6, 1, 3, 2, 4, 7], [7, 1, 5, 3, 6, 4],
              [1, 2, 3, 4, 5], [7, 6, 4, 3, 1]]
    results = [7, 7, 4, 0]

    print(Solution.maxProfit(inputs[0]))
    
    for input, result in zip(inputs, results):
        print("Test: {} = {}".format(input, result))
        assert Solution.maxProfit(input) == result

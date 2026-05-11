class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    #Optimal
    #Using 2 pointers, and checking if the past price is
    #lower then the present,if yes,then calculate the profit
    #(profit = sell price - buy price) else just return 0 

    #keeping the left pointer at index i, and right pointer
    #at i+1 , such that we can check side by side

    #this process is called sliding window
    
        res=0 
        l, r=0,1

        while r < len(prices):
            if  prices[l]<=prices[r]:
                profit=prices[r]-prices[l]
                res=max(res,profit)
            else:
                l=r
            r+=1
        return res

            

            



                
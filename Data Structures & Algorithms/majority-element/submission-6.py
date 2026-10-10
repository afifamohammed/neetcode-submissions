class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        # using boyre moore algo -
        

        # eg - [5,5,1,1,1,5,5]

        count = 0
        res = 0

        for n in nums:
            if count == 0:
                res = n

            count += (1 if n == res else -1)

        return res



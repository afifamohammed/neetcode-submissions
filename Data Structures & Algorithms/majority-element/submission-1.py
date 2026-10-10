class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        # using hashmap
        
        count={}
        res = 0
        MAx=0

        for n in nums:
            count[n] = 1 + count.get(n,0)
            if count[n] > MAx:
                res = n
            
            MAx = max(count[n],MAx)
        return res
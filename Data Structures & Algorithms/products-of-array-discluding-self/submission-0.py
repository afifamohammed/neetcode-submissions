class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        my_dict=defaultdict(int)
        
        res=[]
        for i in range(len(nums)):
            mul=1
            for j in range(len(nums)):
                
                if j==i:
                    continue
                mul*=nums[j]
            res.append(mul)   
        return res


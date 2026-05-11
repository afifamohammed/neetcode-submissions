class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num]=1+count.get(num,0)
        
        Freq=[[] for _ in range(len(nums)+1)]
    
        for key,v in count.items():
            Freq[v].append(key)

        res=[]

        for i in range(len(Freq)-1,0,-1):
            for n in Freq[i]:
                res.append(n)
                if len(res)==k:
                    return res 












    

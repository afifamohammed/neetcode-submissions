class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for num in nums:
            count[num]=1+count.get(num,0)

        FreqBucket=[[] for i in range(len(nums)+1)]
        for num,cnt in count.items():
            FreqBucket[cnt].append(num)

        result=[]
        for i in range(len(FreqBucket)-1,0,-1):
            for num in FreqBucket[i]:
                result.append(num)
                if len(result)==k:
                    return result



        
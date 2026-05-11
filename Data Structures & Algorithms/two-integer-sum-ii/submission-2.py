class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res=[]
        for i in range(len(numbers)):
            for j in range(i+1,len(numbers)):
                if i<j and numbers[i]+numbers[j]==target:
                    res.extend([i+1,j+1])
                    
        return res


        
class Solution:
    def check(self, nums: List[int]) -> bool:
        #BruteForce
        sortednums=sorted(nums)
        arr=[]

        for i in range(len(nums)):
            arr.insert(0,sortednums.pop())
            if nums==arr+sortednums:
                return True
        return False



        
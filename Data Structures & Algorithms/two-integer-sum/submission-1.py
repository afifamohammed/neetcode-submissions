class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        see={}

        for i ,n in enumerate(nums):
            diff=target -n
            if diff in see:
                return[see[diff],i]
            else:
                see[n]=i
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        # Brute Force
        new_num = [n**2 for n in nums]
        new_num.sort()

        return new_num
        
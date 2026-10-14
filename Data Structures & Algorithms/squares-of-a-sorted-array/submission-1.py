class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        # Optimal solution 

        # using 2 pointers to check and set elements in non decreasing order
        # we are squaring and comparing which is largest number at same time , one pass
        # appending the largest into result , later reversoing array because we wanted non decreasing order

        res = []
        l,r = 0,len(nums)-1

        while l<=r:

            if nums[l]*nums[l] > nums [r]*nums[r]:
                res.append(nums[l]*nums[l])
                l +=1

            else:
                res.append(nums[r]*nums[r])
                r -= 1 

        return res[::-1]




        
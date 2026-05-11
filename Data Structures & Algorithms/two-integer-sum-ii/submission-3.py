class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #optimum solution:
        #using pointers to avoid iterating whole list n times
        #where n is list size
        #initializing 2 pointers, 1 at 1st index,2nd at last index
        #adding the values of 2 pointers and checking if it sums up to 
        #the target.
        #if sums up to target , return index+1
        #else if sum > target decreament right pointer with 1
        #else if sum < target increament left pointer with 1

        l,r=0,len(numbers)-1

        while l<r:
            Sum=numbers[l]+numbers[r]
            if Sum>target:
                r-=1
            elif Sum<target:
                l+=1
            else:
                return [l+1,r+1]
        return []



        
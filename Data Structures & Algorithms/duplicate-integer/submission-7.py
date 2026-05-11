class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''a set is used when we have to traverse a list of values so many times,

        because if we traverse n times for every value,time complexity becomes o(n^2)

        so we use a set to avoid traversing n times, and traverse only once for any
        size of n like:

        for each value, check if the value is already exists in set?
        if exists, it means the value have duplicate

        if not , add that value to the set for further checking
        '''

        seen=set()

        for i in nums:
            if i in seen:
                return True
            else:
                seen.add(i)
        return False

       
        
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
    #take an empty set and after checking each number of nums 
    # , append that number to that set

    #this reduces rechecking the whole list each time to check
    #whether duplicates present or not

    #eg: set={}
    #    nums=[1,2,3,4,3]
    #    checks if i is in set{}, 
    #    if presents, returns True (means has a duplicate)
    #    else inserts i into set (storing in set,for futher checking)
        my_set = set()

        for i in nums:
            if i in my_set:
                return True
            else:
                my_set.add(i)
        return False
                
        
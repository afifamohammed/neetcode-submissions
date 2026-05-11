class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #when str1 and str2 both have same characters with different order - True
        #else false
        # save each char of str1 in tempset, if str2 in temp set, returning true

        if len(s)!=len(t):
            return False
        return sorted(s)==sorted(t)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)

        for words in strs:
            FreqArr=[0]*26
            for letter in words:
                FreqArr[ord(letter)-ord('a')]+=1
            res[tuple(FreqArr)].append(words)

        return list(res.values())
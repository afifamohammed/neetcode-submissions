class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #using 2 pointers,for comparing with each pair of 
        #bars where the maximum water stores

        #maximum water=maximum area

        #area =l*b , l is length of each bar, b means
        #difference of both bars(j-i),i,j are indices
        res=0
        l,r=0,len(heights)-1

        while l<r:
            area=min(heights[l],heights[r])*(r-l)
            res=max(res,area)
            if heights[l]<=heights[r]:
                l+=1
            else:
                r-=1
        return res

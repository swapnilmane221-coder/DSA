class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<3:
            return max(nums)
        i=0
        maxarr=[]
        while i<3 and len(nums)>0:
            if max(nums) not in maxarr:
                maxarr.append(max(nums))
                nums.remove(max(nums))
                i+=1
            else:
                nums.remove(max(nums))
        if len(maxarr)<3:
            return max(maxarr)

        return maxarr[-1]
        
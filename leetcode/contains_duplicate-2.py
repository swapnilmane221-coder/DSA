class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        lastoccurence={}
        for i,num in enumerate(nums):
            if num in lastoccurence:
                previous_ind=lastoccurence[num]
                if i-previous_ind<=k:
                    return True
            lastoccurence[num]=i
        return False
            
        
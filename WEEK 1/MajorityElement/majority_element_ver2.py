class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        val = -1
        for num in nums:
            if count != 0 and num == val:
                count = count + 1
            elif count != 0:
                count = count - 1
            else:
                val = num
                count = 1
        return val
                
        

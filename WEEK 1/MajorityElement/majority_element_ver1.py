class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        half = len(nums) / 2
        hash_map = {}
        for num in nums:
            if num not in hash_map:
                hash_map[num] = 0
            hash_map[num] = hash_map[num] + 1
            if (hash_map[num] > half):
                return num
                
        

class Solution:
    def pivotIndex(self, nums):
        total = sum(nums) 

        lSum = 0
        for i in range(len(nums)):
            rSum = total - nums[i] - lSum 
            if lSum == rSum:
                return i
            lSum += nums[i]
        return -1

# runtime: 147 ms, beats: 93.62%

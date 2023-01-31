class Solution:
    def runningSum(self, nums):
        runSum = 0 
        newList = []

        for i in nums:
            runSum += i
            newList.append(runSum)

        return newList
    
# Runtime: 36 ms, Beats: 92.76%

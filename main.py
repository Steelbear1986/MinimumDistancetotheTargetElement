class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        h=sum(nums)
        for i in range(len(nums)):
            if nums[i]==target:
                  h=min(h,abs(i-start))
        return h
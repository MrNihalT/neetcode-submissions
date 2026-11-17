class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = {}
        for i in range(len(nums)):
            n = target-nums[i]
            if n in a:
                return [a[n],i]
            else:
                a[nums[i]] = i
        return False
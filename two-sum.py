class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map = {}
        for i in range(len(nums)):
            implement = target - nums[i]
            if str(implement) in map.keys():
                return [map.get(str(implement)), i]
            map[str(nums[i])] = i


solution = Solution()
print(solution.twoSum([3,4,5,6,7], 10))


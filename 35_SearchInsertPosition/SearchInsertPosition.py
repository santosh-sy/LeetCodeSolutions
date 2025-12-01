from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        position = 0

        if nums[0] == target or target < nums[0]:
            return 0

        for num in range(len(nums)):
            if nums[num] < target:
                continue
            elif nums[num] == target:
                position = num
                return position
            else:
                if position == 0:
                    position = len(nums)

        if position == 0:
            return len(nums)
        else:
            return position

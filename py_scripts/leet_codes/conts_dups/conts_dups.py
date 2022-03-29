from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        values_pres = {}
        for i in range(len(nums)):
            if nums[i] in values_pres:
                return True
            else:
                values_pres[nums[i]] = True
        return False

a = Solution()
print(a.containsDuplicate([1,2,3,1,5]))
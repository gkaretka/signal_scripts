from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for i in range(len(nums1)):
            cnt = nums2.count(nums1[i])
            if cnt > 0:
                res.append(nums1[i])
                nums2.remove(nums1[i])
        return res

a = Solution()
print(a.intersect([1,5,2,4,6,4], [54,5,48,45,4,4]))

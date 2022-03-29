class Solution:
    def rotate(self, nums, k):
        for j in range(k):
            v = nums[0]
            for i in range(1, len(nums)):
                nums[i] = nums[i] ^ v
                v = nums[i] ^ v
                nums[i] = nums[i] ^ v
            nums[0] = v
            print(nums)

a = Solution()

a.rotate([1,2,3,4,5], 2)
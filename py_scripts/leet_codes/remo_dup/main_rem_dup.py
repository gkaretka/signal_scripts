class Solution:
    def removeDuplicates(self, nums):
        prev_val = nums[0]
        piv = 1
        for i in range(1, len(nums)):
            if(prev_val == nums[i]):
                continue
            else:
                nums[piv] = nums[i]
                prev_val = nums[i]
                piv += 1
        return (2, nums)

a = Solution()

n, res = a.removeDuplicates([1,1,3,3,4,4,4])
print(n, res)

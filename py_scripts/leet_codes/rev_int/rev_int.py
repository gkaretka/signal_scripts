class Solution:
    def reverse(self, x: int) -> int:
        new_num = 0
        res_s = ""
        cmp = 2**(32-1)
        if (x < 0):
            neg = -1
        else:
            neg = 1

        if (x == 0):
            return 0

        x = abs(x)
        while x != 0:
            res_s = res_s + str(int(x % 10))
            x = int(x / 10)
        res = int(res_s)*neg

        if abs(res) > cmp:
            return 0
        else:
            return res

a = Solution()
res = a.reverse(1563847412)

print(res)
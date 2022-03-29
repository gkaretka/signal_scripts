class Solution:
    def myAtoi(self, s: str) -> int:
        idx = 0
        while len(s) > 0 and s[0] == ' ':
            s = s[1:len(s)]
            idx += 1

        if len(s) == 0:
            return 0

        mult = 1
        if s[0] == '-':
            mult = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]

        val = 0
        for i in range(len(s)):
            if ord('0') > ord(s[i]) or ord(s[i]) > ord('9'):
                break

            val += ord(s[i]) - 48
            val *= 10
        val /= 10

        res = int(val * mult)
        if res > 2 ** (32 - 1):
            return (2 ** 31 - 1)
        elif res < -2 ** (32):
            return -2 ** 31
        else:
            return res


a = Solution()
#
print(a.myAtoi("   -42"))
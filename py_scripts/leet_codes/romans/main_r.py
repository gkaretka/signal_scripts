class Solution:
    def romanToInt(self, s: str) -> int:
        fin_sum = 0

        prev_val = self.convertVal(s[0])
        par_sum = prev_val

        for i in range(1, len(s)):
            cur_val = self.convertVal(s[i])
            if cur_val == prev_val:
                par_sum += cur_val
            elif cur_val < prev_val:
                fin_sum += par_sum
                par_sum = 0
            elif cur_val > prev_val:
                fin_sum += (cur_val - par_sum)
                par_sum = 0

            prev_val = cur_val

        fin_sum += par_sum
        return fin_sum

    def convertVal(self, s: str) -> int:
        if s == "I":
            return 1
        elif s == "V":
            return 5
        elif s == "X":
            return 10
        elif s == "C":
            return 100
        elif s == "D":
            return 500
        elif s == "M":
            return 500
        else:
            return 0

a = Solution()

print(a.romanToInt("III"))
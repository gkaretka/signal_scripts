class Solution:
    def firstUniqChar(self, s: str) -> int:
        chars = {}
        idxs = []
        for i in range(len(s)):
            if s[i] in chars:
                chars[s[i]] = chars[s[i]] + 1
            else:
                chars[s[i]] = 1
                idxs.append(i)

        idx = 0
        for val in chars.values():
            if val == 1:
                return idxs[idx]
            idx += 1

        return -1

a = Solution()
print(a.firstUniqChar("dddccdbba"))
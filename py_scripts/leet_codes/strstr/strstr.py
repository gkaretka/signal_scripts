class SolutionA:
    def strStr(self, haystack: str, needle: str) -> int:
        if (len(haystack) == 0 and len(needle) == 0) or len(needle) == 0:
            return 0

        i = 0
        while i < len(haystack):
            match = False
            if haystack[i] == needle[0]:
                match = True
                for j in range(0, len(needle)):
                    if i + j > len(haystack) - 1:
                        return -1
                    if haystack[i + j] != needle[j]:
                        match = False
                        i += j-1
                        break
            else:
                i += 1
            if match:
                return i
        return -1


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        M = len(needle)
        N = len(haystack)

        lps = self.tabtab(needle)

        i = 0
        j = 0
        while i < N:
            if needle[j] == haystack[i]:
                i += 1
                j += 1
            if j == M:
                return i - j
            elif i < N and needle[j] != haystack[i]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1

    def tabtab(self, needle):
        i = 1
        tab = [0]
        while i < len(needle):
            ss = needle[0:i+1]
            cnt = len(ss) - 1
            while ss[0:cnt] != ss[len(ss)-cnt:len(ss)]:
                cnt -= 1
            tab.append(cnt)

            i += 1

        return tab

a = Solution()
print(a.tabtab("aabaacaabaa"))
print(a.tabtab("aaabaaa"))
#print("res", a.strStr("mississippi", "issip"))
#print("res2", a.strStr("mississippi", "sipp"))

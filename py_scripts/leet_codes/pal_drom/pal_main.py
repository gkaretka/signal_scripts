class Solution:
    def isPalindrome(self, s: str) -> bool:
        val_chars = list(range(ord('a'), ord('z')+1))
        val_chars += list(range(ord('0'), ord('9')+1))
        s = s.lower()
        i = 0
        while i < len(s):
            if ord(s[i]) not in val_chars:
                s = s.replace(s[i], "")
                i-=1
            i+=1

        adder = 0
        if len(s) % 2 != 0:
            adder = 1

        c = int(len(s)/2)
        s1 = s[0:c]
        s2 = s[c+adder:len(s)]
        s2 = s2[::-1]

        if s1 == s2:
            return True
        else:
            return False

a = Solution()

#s = "race a car"                       # not
#s = "A man, a plan, a canal: Panama"    # yes
#s = " "                                # yes
#s = "aa"
#s = "a."
#s = "ab@a"
#s = "0P"
s = "9,8"
print(a.isPalindrome(s))
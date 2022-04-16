"""
write a function foo(s) which for every char c in s prints the length of the longest sequence of consecutive occurence of c in s
example:
foo("aabbbxxbbaaaaax")
a : 5
b : 3
x : 2
"""

def foo(s):
    vals = {}

    cnt = 1
    cur_char = s[0]
    for i in range(1, len(s)):
        if s[i] == cur_char:
            cnt += 1
        else:
            if vals.get(ord(cur_char), 0) < cnt:
                vals[ord(cur_char)] = cnt

            cur_char = s[i]
            cnt = 1

    return vals

print(foo("aabbbxxbbaaaaax"))
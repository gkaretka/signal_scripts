s = "uihoudaaaabcbcbcbcdwabacbccuioinababcch"
subs = "abc"

i = 0
while i < len(s):
    if s[i:i+len(subs)] == subs:
        s = s[0:i] + s[i+len(subs):-1]
        i = i - len(subs)
    else:
        i += 1


def test_it(_s: str, _substr: str):
    while s.count(_substr) > 0:
        _s = _s.replace(_substr, "")

    print(_s)


test_it(s, subs)
print(s)

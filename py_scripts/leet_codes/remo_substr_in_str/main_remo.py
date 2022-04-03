s = "daabcbaabcbc"
subs = "abc"

def perform(_s: str, _subs: str):
    stck = ""

    i = 0
    while i < len(_s):
        stck += _s[i]
        while stck[len(stck)-len(_subs):len(stck)] == _subs:
            stck = stck.removesuffix(_subs)
        i += 1

    print(stck)



def test_it(_s: str, _substr: str):
    while _s.count(_substr) > 0:
        _s = _s.replace(_substr, "")

    print(_s)


perform(s, subs)
test_it(s, subs)

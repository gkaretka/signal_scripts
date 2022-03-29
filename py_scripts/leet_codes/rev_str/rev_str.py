from typing import List


class SolutionA:
    def reverseString(self, s: List[str]) -> None:
        for i in range(int(len(s)/2)):
            tmp = s[i]
            s[i] = s[len(s)-i-1]
            s[len(s)-i-1] = tmp

class SolutionB:
    def reverseString(self, s: List[str]) -> str:
        if len(s) > 1:
            return s[len(s)-1], self.reverseString(s[:-1])

a = SolutionB()
print(a.reverseString(list("Hello, World!")))
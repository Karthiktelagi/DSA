class Solution:
    def isValid(self, s: str) -> bool:
        prev = ""

        while s != prev:
            prev = s
            s = s.replace("()", "").replace("[]", "").replace("{}", "")

        return s == ""
# https://leetcode.com/problems/process-string-with-special-operations-i/description/

def clean(s):
    s = list(s)
    prev_char = s[0]
    for i in range(1, len(s)):
        if prev_char == s[i] == "%":
            s[i-1], s[i] = "", ""
            prev_char = ""
        else:
            prev_char = s[i]
    return "".join(s)

class Solution:
    def processStr(self, s: str) -> str:
        s = clean(s)
        processed_s = []
        for char in s:
            if char == "*":
                if processed_s:
                    processed_s.pop()
            elif char == "#":
                processed_s.extend(processed_s)
            elif char == "%":
                processed_s.reverse()
            else:
                processed_s.append(char)
        return "".join(processed_s)
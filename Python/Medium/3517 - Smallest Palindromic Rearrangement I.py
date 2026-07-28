# https://leetcode.com/problems/smallest-palindromic-rearrangement-i/description/

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        if len(s) == 1: return s
        distinct_letters = sorted(list(set(s)))
        letter_counts = {letter : s.count(letter) for letter in distinct_letters}
        return (
            "".join([letter * (letter_counts[letter] // 2) for letter in distinct_letters])
            + "".join([letter for letter in distinct_letters if letter_counts[letter] % 2 != 0])
            + "".join([letter * (letter_counts[letter] // 2) for letter in distinct_letters[::-1]])
        )
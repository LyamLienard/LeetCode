# https://leetcode.com/problems/weighted-word-mapping/description/

class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        # a -> 97
        word_weights = []
        for word in words:
            word_weights.append(sum([weights[ord(letter) - ord("a")] for letter in word]) % 26)
        
        concatenated_string = ""
        for weight in word_weights:
            concatenated_string += chr(ord("z") - weight)
        
        return concatenated_string

# Compacted alternative, for fun :
# class Solution:
#     def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
#         concatenated_string = ""
#         for word in words:
#             concatenated_string += chr(ord("z") - sum([weights[ord(letter) - ord("a")] for letter in word]) % 26)
#         return concatenated_string
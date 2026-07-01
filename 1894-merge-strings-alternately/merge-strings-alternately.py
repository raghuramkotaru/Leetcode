# class Solution:
#     def mergeAlternately(self, word1: str, word2: str) -> str:
        


#         def mer(w1,w2):
#             res = ""
#             i=0
#             ma = min(len(w1),len(w2))
#             while i<ma:
#                 res += w1[i]
#                 res += w2[i]
#                 i += 1
#             if i< len(w1):
#                 res+= w1[i:]
#             if i< len(w2):
#                 res+= w2[i:]
#             return res
#         return mer(word1,word2)
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []

        for a, b in zip(word1, word2):
            merged.append(a + b)
        
        merged.append(word1[len(word2):])
        merged.append(word2[len(word1):])

        return "".join(merged)



class Solution:
    def possibleStringCount(self, word: str) -> int:
        t = 0
        for i in range(len(word) - 1):
            if word[i] == word[i + 1]:
                t+=1
        return t+1

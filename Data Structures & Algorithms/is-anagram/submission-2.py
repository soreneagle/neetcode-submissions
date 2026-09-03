class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters_s = []
        letters_t = []
        for i in s:
            letters_s.append(i)
        letters_s.sort()
        for j in t:
            letters_t.append(j)
        letters_t.sort()

        if letters_s == letters_t:
            return True
        else:
            return False
        
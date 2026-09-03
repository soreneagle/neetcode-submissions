class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sort_s = []
        sort_t = []

        for i in s:
            sort_s.append(i)
        for j in t:
            sort_t.append(j)

        sort_s.sort()
        sort_t.sort()

        if sort_s == sort_t:
            return True
        return False
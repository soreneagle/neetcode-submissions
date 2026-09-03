class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): # if the lengths are diff they cant be anagrams
            return False

        countS = {} # initialize count s
        countT = {} # initialize count t

        for i in range(len(s)): # both s and t are same length
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT
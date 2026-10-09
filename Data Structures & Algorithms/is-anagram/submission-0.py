class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        chars_s = set(s)
        chars_t = set(t)           
        for c in chars_t:
            count_s = s.count(c)
            count_t = t.count(c)
            if count_s != count_t:
                return False
        return True       
        
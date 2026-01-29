class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t_set = set(t)
        s_set = set(s)

        unique_chars = t_set ^ s_set
        if len(unique_chars)==0:
            if len(s)==len(t):
                for elm in s :
                    if s.count(elm)==t.count(elm):
                        return True
                    else:
                        return False
            else: return False
        else: return False

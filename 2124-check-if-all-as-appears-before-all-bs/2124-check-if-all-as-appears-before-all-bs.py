class Solution:
    def checkString(self, s: str) -> bool:
        ok = False
        for i in range(len(s)):
            if s[i] == "a" and ok == True:
                return False
            elif s[i] == "a" and ok == False:
                continue
            elif s[i] == "b":
                ok = True
        return True
        


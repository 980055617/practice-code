class Solution:
    def isValid(self, s: str) -> bool:
        n_map = {"(":0,"[":0,"{":0}
        for i in s:
            if i == "(" or i == "[" or i == "{":
                n_map[i] += 1
            else:
                if i == ")":
                    if n_map["("] <= 0:
                        return False
                elif i == "]":
                    if n_map["["] <= 0:
                        return False
                elif i == "}":
                    if n_map["{"] <= 0:
                        return False
        return True
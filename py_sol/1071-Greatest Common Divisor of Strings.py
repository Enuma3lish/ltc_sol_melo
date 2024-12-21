from math import gcd
def gcdOfStrings(self, str1: str, str2: str) -> str:
    max_len = 0
    if len(str1+str2) != len(str2+str1):
        return ""
    else:
        max_len= gcd(len(str1), len(str2))
    return gcd(str1[:max_len])
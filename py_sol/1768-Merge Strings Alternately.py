def mergeAlternately(word1: str, word2: str) -> str:
        min_len = min(len(word1), len(word2))
        result = ""
        for i in range(min_len):
            result += word1[i] + word2[i]
        result+= word1[min_len:] + word2[min_len:]
        return result
    
result = mergeAlternately("ab","cdef")
print(result)
def reverseVowels(self, s: str) -> str:  
        l=0
        r=len(s)-1
        s=list(s)
        
        while l<r:
            while l<r and s[l] not in "AEIOUaeiou":
                l=l+1
                
            while l<r and s[r] not in "AEIOUaeiou":
                r=r-1
                
            if l<r:
                s[l],s[r]=s[r],s[l]
                l=l+1
                r=r-1
                
        return "".join(s)
#ref:https://ithelp.ithome.com.tw/articles/10286034
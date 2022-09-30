class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        results = ''
       
        if s.isspace():
            return True
        
        for i in s:
            if i.isalnum():
                results += i.lower()
        
        if results[::-1] == results:
            
            return True
        
        else: 
            
            return False

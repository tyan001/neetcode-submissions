class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x<0:
            return False
        if x<9:
            return True

        
        
        div = 1
        while x>=10*div:
            
            div = div * 10
        

        while x:
            left_num = x//div
            right_num= x%10

            if left_num != right_num:
                return False
            
            x = x%div # removes leading
            x = x//10 # removes last
            div = div//100
        
        return True

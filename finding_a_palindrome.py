def isPalindrome(x):
        if(x<0):
            return False
        result=0
        original=x
        while x!=0:
            result=result*10+x%10
            x=x//10
        if(original==result):
            return True
        else:
            return False

print(isPalindrome(121))
print(isPalindrome(10))
# description
# Password Strength Validator
# Problem Description
# A website checks the strength of passwords. A password is considered strong if it satisfies the following rules:
# Length must be at least 8 characters
# Must contain at least one uppercase letter
# Must contain at least one digit
# Must contain at least one special character (@, #, $)
# Given a list of passwords, return a list containing only strong passwords.

class Solution:
    def strong_passwords(self, passwords):
        strong = []
        ## Write your code here
        
        for pwd in passwords:
            if (len(pwd) >= 8 and
                any(c.isupper() for c in pwd) and
                any(c.isdigit() for c in pwd) and
                any(c in "@#$" for c in pwd)):
                
                strong.append(pwd)
        return strong

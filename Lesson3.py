#input variables lowercase
S1 = input("Type Sentence Here: ")
S1 = S1.lower()

S2 = (S1[::-1])
S2 = S2.lower()

#input variables with no white space
NSstring1 = S1.replace(" ", "")
NSstring2 = S2.replace(" ", "")

#palindrome function to compare the input variables
def palindrome(NSstring1, NSstring2):
    if NSstring1 == NSstring2:
        return 'This phrase is a palindrome'
    else:
        return 'This phrase is not a palindrome'


#call palindrome function
TorF = palindrome(NSstring1, NSstring2)
print(TorF)

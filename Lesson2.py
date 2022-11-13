#function to compare input to eachother
def compare(W1, W2):
    if (
            sorted(W1) == sorted(W2)
    ):
        print(" These words are anagrams ")
    else:
        print("the words aren't anagrams")

#input variables
W1 = input('type word 1 here: ')
W2 = input('type word 2 here: ')

#call compare function
compare(W1, W2)


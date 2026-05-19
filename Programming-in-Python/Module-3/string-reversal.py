#Slice function

word = "reversal"
new_trial = word[::-1]
print(new_trial)

#Recursive function

def reverse_string(word):
    if len(word) == 0: 
        return word
    else:
        return reverse_string(word[1:]) + word[0]
    
reverse_word = reverse_string(word)
print(reverse_word)
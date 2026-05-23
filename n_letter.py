def nth_char(words):
    return ''.join(word[n] for n, word in enumerate(words))
 
 
words = input("Enter words separated by spaces: ").split()
print(nth_char(words))

def nth_char(words):
    return ''.join(word[n] for n, word in enumerate(words))
 
if __name__ == "__main__":
    words = input("Enter words separated by spaces: ").split()
    print(nth_char(words))


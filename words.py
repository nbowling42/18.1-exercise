def print_upper_words(words, set):
    """ Takes a list of words and prints them all out on a seperate line all uppercased """
    for word in words:
        if word[0] in set:
            print(word.upper())

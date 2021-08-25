def capitalize(string):
    """My solution"""
    words = string.split()
    for ind, word in enumerate(words):
        words[ind] = word[0].upper() + word[1:]
    return ' '.join(words)

def capitalize(word):
    first_letter_small = word[0]
    first_letter_big = chr(ord(first_letter_small) - ord('a') + ord('A'))
    return first_letter_big + word[1:]

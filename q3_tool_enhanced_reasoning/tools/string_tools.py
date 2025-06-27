def count_vowels(word):
    return sum(1 for ch in word.lower() if ch in "aeiou")

def count_letters(word):
    return len([ch for ch in word if ch.isalpha()])

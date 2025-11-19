# how to check whether a word only uses the available letters


def use_only(letters, word):
    """Return True if the word only uses the given letters, return False otherwise

    letters = 'kroiacm'
    word = 'abcd'

    for each letter in word, check it is in the given letters
        if it is in the given letters, do nothing
        if it is not in the given letters, return False
    """
    for letter in word:
        if letter not in letters:
            return False
    return True


# print(use_only("kroiacm", "abcd"))  # False
# print(use_only("kroiacm", "roam"))  # True


def spelling_bee():
    """Print all the words that are at least 4 letters long, contain the letter 'm',
    and only use the letters in 'kroiacm'"""
    # words = ["abcd", "roam", "xyz", "aaaaaa", "room", "mad"]

    with open("data/words.txt") as f:
        words = f.read().splitlines()
    # print(words)
    available_letters = "kroiacm"
    for word in words:
        if len(word) >= 4 and "m" in word and use_only(available_letters, word):
            print(word)


spelling_bee()

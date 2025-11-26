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


def at_least(word, n):
    return len(word) >= n


def must_use(word, letter):
    return letter in word


def spelling_bee(available_letters, required_letter):
    """Print all the words that are at least 4 letters long, contain the letter 'm',
    and only use the letters in 'kroiacm'"""
    # words = ["abcd", "roam", "xyz", "aaaaaa", "room", "mad"]

    with open("data/words.txt") as f:
        words = f.read().splitlines()
    # print(words)

    for word in words:
        if (
            at_least(word, 4)
            and must_use(word, required_letter)
            and use_only(available_letters, word)
        ):
            print(word)


def solve():
    available_letters = input("What are the available letters: ")
    required_letter = input("What is the required letter: ")
    spelling_bee(available_letters, required_letter)


solve()

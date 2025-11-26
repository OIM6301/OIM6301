import webbrowser


def rotate(word, n):
    """
    Take a string, WORD, and an integer, N as parameters,
    return a new string that contains the letters from the original
    string, WORD, rotated by the given amount, N.
    """
    s = ""
    for c in word:
        if c.isalpha():
            if c.islower():
                shift = (ord(c) - ord("a") + n) % 26
                s += chr(ord("a") + shift)
            else:
                shift = (ord(c) - ord("A") + n) % 26
                s += chr(ord("A") + shift)
        else:
            s += c
    return s


def solve_puzzle_01():
    """
    http://www.pythonchallenge.com/pc/def/map.html
    """
    message = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
    print(rotate(message, 2))
    
    url = "http://www.pythonchallenge.com/pc/def/map.html"
    new_url = url.replace("map", rotate("map", 2))
    webbrowser.open(new_url)


def main():
    print(rotate("abc", 2))
    print(rotate("xyz", 2))
    print(rotate("0-9, A-Z", 2))
    solve_puzzle_01()


if __name__ == "__main__":
    main()

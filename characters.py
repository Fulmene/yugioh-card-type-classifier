chars = [
            'a', 'b', 'c', 'd', 'e', 'f',
            'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x',
            'y', 'z', ',', ' '
        ]

rev_chars = dict((c, i) for i, c in enumerate(chars))

def char2ind(char):
    return rev_chars[char]

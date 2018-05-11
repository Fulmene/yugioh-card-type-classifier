import csv

chars = [
         ' ', '!', '"', '#', '%', "'", ',',
         '-', '.', '/', '0', '1', '2', '3',
         '4', '5', '6', '7', '8', '9', ':',
         '=', '?', 'a', 'b', 'c', 'd', 'e',
         'f', 'g', 'h', 'i', 'j', 'k', 'l',
         'm', 'n', 'o', 'p', 'q', 'r', 's',
         't', 'u', 'v', 'w', 'x', 'y', 'z',
         'é', 'ñ', 'ú', 'ü', 'α', 'β', 'ω',
         '☆', '・'
        ]

rev_chars = dict((c, i+1) for i, c in enumerate(chars))

def char2ind(char):
    if char in rev_chars:
        return rev_chars[char]
    else:
        return 0

card_types = [ 'Monster', 'Spell', 'Trap' ]

rev_card_types = dict((c, i) for i, c in enumerate(card_types))

def type2ind(card_type):
    return rev_card_types[card_type]

def load_data(data_path='data/card_types.csv', train_ratio=0.8, val_ratio=0.1):
    with open(data_path, 'r') as datafile:
        data_dict = dict(csv.reader(datafile, quotechar='^', delimiter=','))

    # Filter out alternate versions of cards
    data = list(filter(lambda x: '(' not in x[0], data_dict.items()))

    train_last = int(train_ratio * len(data))
    val_last = train_last + int(val_ratio * len(data))

    train_data = data[:train_last]
    val_data = data[train_last:val_last]
    test_data = data[val_last:]

    return train_data, val_data, test_data

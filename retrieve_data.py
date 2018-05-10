import csv
import random
import pickle
import os.path
import requests

base_url = 'https://www.ygohub.com/api/'

if os.path.isfile('data/card_names.pkl'):
    r = requests.get(base_url + 'all_cards')
    if r.status_code == 200:
        obj = r.json()
        cards = obj['cards']
        with open('data/card_names.pkl', 'wb') as dumpfile:
            pickle.dump(cards, dumpfile)
    else:
        exit()
else:
    with open('data/card_names.pkl', 'rb') as dumpfile:
        cards = pickle.load(dumpfile)

random.shuffle(cards)
with open('data/card_types.csv', 'w') as typefile:
    for i, card_name in enumerate(cards):
        if i%100 == 0:
            print(i)
        status = 404
        while status != 200:
            name_req = requests.get(base_url + 'card_info?name=' + card_name)
            status = name_req.status_code
        obj = name_req.json()
        if 'card' in obj:
            card = obj['card']
            typefile.write('"')
            typefile.write(card_name)
            typefile.write('",')
            typefile.write(card['type'])
            typefile.write('\n')

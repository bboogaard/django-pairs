"""
Organize the cards into a deck.

"""
import random


image_urls = [
    'pairs/images/abarth.png',
    'pairs/images/alfa-romeo.png',
    'pairs/images/audi.png',
    'pairs/images/bmw.png',
    'pairs/images/dacia.png',
    'pairs/images/fiat.png',
    'pairs/images/ford.png',
    'pairs/images/mercedes-benz.png',
    'pairs/images/opel.png',
    'pairs/images/toyota.png'
]


def shuffle():
    """Return a list of randomly sorted cards."""
    deck = []
    lst = list(range(1, len(image_urls) + 1))

    for i in range(2):
        random.shuffle(lst)
        for ii in lst:
            deck.append({
                'id': ii,
                'image_url': image_urls[ii - 1]
            })

    return deck

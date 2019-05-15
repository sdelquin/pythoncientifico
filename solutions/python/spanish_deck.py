import itertools

DECK_NUMBERS = range(1, 13)
DECK_SUITS = ('OROS', 'COPAS', 'ESPADAS', 'BASTOS')

for number, suit in itertools.product(DECK_NUMBERS, DECK_SUITS):
    print(f'{number:>2} de {suit}')

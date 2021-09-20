"""The deck of cards and all possible cards."""
from __future__ import annotations
from dataclasses import dataclass
from random import choices


@dataclass
class Card:
    val: int
    name: str
    suit: str

    def __repr__(self):
        return f'{self.name} of {self.suit}'

    def __hash__(self):
        return hash(str(self))


def _mk_set(suit: str) -> list[Card]:
    """Make a set of the given suit."""
    return [
        Card(2, '2', suit),
        Card(3, '3', suit),
        Card(4, '4', suit),
        Card(5, '5', suit),
        Card(6, '6', suit),
        Card(7, '7', suit),
        Card(8, '8', suit),
        Card(9, '9', suit),
        Card(10, '10', suit),
        Card(10, 'jack', suit),
        Card(10, 'queen', suit),
        Card(10, 'king', suit),
        Card(11, 'ace', suit),
    ]


ALL_CARDS = (
    _mk_set('spades') +
    _mk_set('diamonds') +
    _mk_set('hearts') +
    _mk_set('clubs')
)


class Deck:

    def __init__(self, n_sets: int = 5):
        """Initialise a full deck of cards with n_sets of each card."""
        self.n_sets = n_sets
        self.cards = {
            c: n_sets
            for c in ALL_CARDS
        }
        self.total = len(ALL_CARDS) * n_sets

    def deal(self) -> Card:
        """Get a card from the deck."""
        if not self.total:
            print('Deck low, re-shuffling')
            self.shuffle()
        card = choices(
            list(self.cards),
            [v / self.total for v in self.cards.values()],
            k=1
        )[0]
        self.cards[card] -= 1
        self.total -= 1
        return card

    def shuffle(self):
        """Rest all probabilities of the deck."""
        for card in self.cards:
            self.cards[card] = self.n_sets
        self.total = 52 * self.n_sets

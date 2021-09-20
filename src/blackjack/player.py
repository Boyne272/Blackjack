"""Class for the player, with a score and a valid hand."""
from typing import Callable
from blackjack.deck import Card


class Player:
    """Holds the players score and hand."""

    def __init__(
        self,
        name: str = 'player',
        strategy: Callable = None
    ):
        self.name = name
        self.strategy = strategy
        self.hand = []
        self.score = 0

    def __repr__(self):
        return f'{self.name} has {self.hand} ({self.score})'

    def lower_ace(self) -> bool:
        """If an ace is present lower the value of this hand."""
        for card in self.hand:
            if card.val == 11:
                print('lowering ace from 11 -> 1')
                self.score -= 10
                card.val = 1  # val not included in card hash, so this is safe
                return True
        return False

    def add_to_hand(self, card: Card) -> bool:
        """Add the given card to the hand."""
        self.hand.append(card)
        self.score += card.val
        if self.score > 21 and not self.lower_ace():
            print(f'Score {self.score} {self.name} Bust!')
            return False
        return True

    def reset(self):
        """Clear the players hand and score."""
        self.hand = []
        self.score = 0

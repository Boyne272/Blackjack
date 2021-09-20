"""Dummy script to test setup."""
from __future__ import annotations
import os

from blackjack.deck import Deck, Card
from blackjack.player import Player


class Game:
    """Play a simple game of blackjack with the env var settings."""

    def __init__(self, players: list[Player]):
        self.deck = Deck()
        self.players = players

    def new_hand(self):
        """Deal a new hand for all players."""
        for p in self.players:
            p.reset()  # reset all hands
            p.add_to_hand(self.deck.deal())
            p.add_to_hand(self.deck.deal())

    def showdown(self):
        scores = [p.score for p in self.players if p.score <= 21]
        if not scores:
            print('all players bust')
            return
        best = max(scores)
        for p in self.players:
            if p.score == best:
                print('player %s has won 🥳' % p.name)

    def __call__(self):
        """Play a game."""
        self.new_hand()
        for p in self.players[::-1]:
            hit = True
            print(f'\t {p}')
            while p.score < 21 and hit:
                hit = (
                    _get_input('Hit or Stick', ('h', 's')) == 'h'
                    if not p.strategy
                    else p.strategy(p)
                )
                if hit:
                    p.add_to_hand(self.deck.deal())
                    print(f'\t {p}')
        self.showdown()


def _get_input(s: str, options: tuple[str] = ('y', 'n')):
    """Get user input as one of the given options."""
    while (input_ := input(f'{s} ({", ".join(options)}): ')) not in options:
        print('Invalid input, try again')
    return input_


if __name__ == "__main__":
    players = [Player('dealer', strategy=lambda p:p.score < 17)]
    print('enter player names or blank for no players')
    while name := input(f'Player {len(players)} name: '):
        players.append(Player(name))

    g = Game(players)
    while _get_input('Deal hand') == 'y':
        print('-' * 20)
        g()

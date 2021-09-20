"""A dummy test script."""

from src.blackjack.deck import Deck
from src.blackjack.deck import ALL_CARDS
from pytest import raises


def test_deck_init():
    """Ensure the deck is initialized with the right number of cards."""
    d = Deck(2)
    assert len(d.cards) == 52, 'should be 52 unique cards in the deck'
    assert d.total == 52 * 2, 'should be this many total cards present'
    assert all(v == 2 for v in d.cards.values())


def test_deck_deal():
    """Ensure we get a single card from the deck as expected."""
    d = Deck(1)
    card = d.deal()
    assert card in ALL_CARDS
    assert d.total == 51
    assert sum(d.cards.values()) == 51


def test_deck_reshuffle():
    """Ensure we can get all cards from the deck as expected."""
    d = Deck(1)
    all_cards = [
        d.deal()
        for _ in range(52)
    ]
    assert set(all_cards) == set(ALL_CARDS), 'should be one of each card'

    with raises(ValueError):
        d.deal()  # no cards left in deck
    assert d.total == 0
    assert all(v == 0 for v in d.cards.values())

    d.shuffle()
    assert d.deal() in all_cards, 'should see a card again'

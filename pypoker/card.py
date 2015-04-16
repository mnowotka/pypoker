__author__ = 'mnowotka'

import re
from random import randint
try:
    from termcolor import colored
except ImportError:
    colored = None

#------------------------------------------------------------------------------


class CardException(Exception):
    pass

#------------------------------------------------------------------------------


class Card(object):

    ranks = [
        [u'1', 1, 'One'],
        [u'2', 2, 'Two'],
        [u'3', 3, 'Three'],
        [u'4', 4, 'Four'],
        [u'5', 5, 'Five'],
        [u'6', 6, 'Six'],
        [u'7', 7, 'Seven'],
        [u'8', 8, 'Eight'],
        [u'9', 9, 'Nine'],
        [u'10', 10, 'Ten'],
        [u'J', 11, 'Jack'],
        [u'Q', 12, 'Queen'],
        [u'K', 13, 'King'],
        [u'A', 14, 'Ace'],
    ]

    suits = [
        [[u'C', u'\u2663', u'\u2667'], 1, 'Clubs'],
        [[u'D', u'\u2666', u'\u2662'], 2, 'Diamons'],
        [[u'H', u'\u2665', u'\u2661'], 3, 'Hearts'],
        [[u'S', u'\u2660', u'\u2664'], 4, 'Spades'],
    ]

    card_re = re.compile('(?P<rank>\d{,2}|[JQKA])(?P<suit>[CDHS])')

    def __init__(self, rank=None, suit=None, black=True, fourColors=False):
        ranks = dict([(r[0], r[1]) for r in self.ranks])
        suits = dict()
        self.fourColors = fourColors
        self.black = black
        for s in self.suits:
            for ch in s[0]:
                suits[ch] = s[1]
        try:
            if rank and suit:
                self.rank = ranks[rank]
                self.suit = suits[suit]
            elif rank:
                if type(rank) == Card:
                    self.rank = rank.rank
                    self.suit = rank.suit
                else:
                    match = self.card_re.match(rank)
                    if not match:
                        raise CardException()
                    else:
                        d = match.groupdict()
                        self.rank = ranks[d['rank']]
                        self.suit = suits[d['suit']]
            elif not rank and not suit:
                self.rank = randint(1, len(self.ranks))
                self.suit = randint(1, len(self.suits))
            else:
                raise CardException()
        except KeyError:
            raise CardException()

    def getColor(self):
        if self.fourColors:
            return ['green', 'blue', 'red', 'white'][self.suit - 1]
        else:
            return ['white', 'red', 'red', 'white'][self.suit - 1]

    def __str__(self):
        ranks = dict([(r[1], r[0]) for r in self.ranks])
        suits = dict([(s[1], s[0][0]) for s in self.suits])
        rep = "%s%s" % (ranks[self.rank], suits[self.suit])
        if not colored:
            return rep
        else:
            return colored(rep, self.getColor())

    def __repr__(self):
        return "\"%s\"" % self.symbol

    def __unicode__(self):
        ranks = dict([(r[1], r[0]) for r in self.ranks])
        suits = dict([(s[1], s[0][1]) for s in self.suits]) if self.black else \
            dict([(s[1], s[0][2]) for s in self.suits])
        rep = u"%s%s" % (ranks[self.rank], suits[self.suit])
        if not colored:
            return rep
        else:
            return colored(rep, self.getColor())

    def name(self):
        ranks = dict([(r[1], r[2]) for r in self.ranks])
        suits = dict([(s[1], s[2]) for s in self.suits])
        return "%s of %s" % (ranks[self.rank], suits[self.suit])

    @property
    def symbol(self):
        ranks = dict([(r[1], r[0]) for r in self.ranks])
        suits = dict([(s[1], s[0][0]) for s in self.suits])
        rep = "%s%s" % (ranks[self.rank], suits[self.suit])
        return rep

    def isFaceCard(self):
        return self.rank > 9

    def __hash__(self):
        return self.rank * len(self.ranks) + self.suit

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.rank and other.rank and self.suit and other.suit:
            return self.rank == other.rank and self.suit == other.suit
        return False

    def __neq__(self, other):
        if not isinstance(other, self.__class__):
            return True
        if self == other:
            return False
        if self.rank and other.rank:
            if self.rank != other.rank:
                return True
            if self.suit and other.suit:
                if self.suit != other.suit:
                    return True
                return False
            return False
        return False

    def __gt__(self, other):
        if not isinstance(other, self.__class__): 
            return False
        if not self.rank or not other.rank:
            return False
        if self.rank > other.rank:
            return True
        if self.rank < other.rank:
            return False
        if not self.suit or not other.suit:
            return False
        if self.suit > other.suit:
            return True
        return False

    def __ge__(self, other):
        return self == other or self > other

    def __lt__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if not self.rank or not other.rank:
            return False
        if self.rank < other.rank:
            return True
        if self.rank > other.rank:
            return False
        if not self.suit or not other.suit:
            return False
        if self.suit < other.suit:
            return True
        return False

    def __le__(self, other):
        return self == other or self < other
   

#------------------------------------------------------------------------------

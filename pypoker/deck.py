__author__ = 'mnowotka'

from random import shuffle as shuf
from itertools import product
from pypoker.card import Card
from pypoker.hand import Hand

#------------------------------------------------------------------------------


class Deck(list):
    def __init__(self, start="2", end="A", from_list=None):
        if not from_list:
            list.__init__(self)
            start_idx = [x[0] for x in Card.ranks].index(start)
            end_idx = [x[0] for x in Card.ranks].index(end)
            assert(start_idx < end_idx)
            ranks = [x[0] for x in Card.ranks[start_idx:end_idx+1]]
            cards = ["%s%s" % p for p in
                     product(ranks, [s[0][0] for s in Card.suits])]
        else:
            cards = from_list

        for card in cards:
            self.append(Card(card))

    def shuffle(self):
        shuf(self)

    def burn(self):
        self.pop()

    def deal(self, size, number, deck=False):
        assert(size*number <= len(self))
        for i in range(number):
            chunk = Deck(from_list=[x.symbol for x in self[-size:]])
            del self[-size:]
            yield chunk if deck else Hand(chunk)

    def __contains__(self, item):
        return super(Deck, self).__contains__(Card(item))

    def __str__(self):
        return '[' + ', '.join([str(x) for x in self[::-1]]) + ']'

    def __unicode__(self):
        return '[' + ', '.join([unicode(x) for x in self[::-1]]) + ']'


#------------------------------------------------------------------------------

def ACTUAL_ORDER(PBNS, IAT,IBOND, BTYPE):
    return ( PBNS.edge[PBNS.vert[IAT].iedge[IBOND]].flow + BOND_TYPE_SINGLE if (PBNS and PBNS.edge and PBNS.vert and (BTYPE == BOND_ALT_123 or BTYPE == BOND_ALT_13 or BTYPE == BOND_ALT_23)) else BTYPE)
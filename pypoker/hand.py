__author__ = 'mnowotka'

from pypoker.card import Card

#------------------------------------------------------------------------------


class Hand(set):
    def __init__(self, card_list):
        set.__init__(self, [Card(x) for x in card_list])

    def __str__(self):
        return '{' + ', '.join([str(x) for x in self]) + '}'

    def __unicode__(self):
        return '{' + ', '.join([unicode(x) for x in self]) + '}'

    def __repr__(self):
        return '[' + ', '.join([repr(x) for x in self]) + ']'

    def __contains__(self, item):
        return super(Hand, self).__contains__(Card(item))

#------------------------------------------------------------------------------

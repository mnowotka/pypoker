__author__ = 'mnowotka'

#------------------------------------------------------------------------------


class PokerEvaluator(object):

    def sklansky_rank(self, hand):
        """
        Description here: http://en.wikipedia.org/wiki/Texas_hold_%27em_starting_hands
        """
        if len(hand) != 2:
            return None
        c1 = hand.pop()
        c2 = hand.pop()

    def chan_rank(self, hand):
        """
        The "Chen Formula" is a way to compute the "power ratings" of starting hands that was originally developed
        by Bill Chen
        """
        if len(hand) != 2:
            return None
        rank = 0
        c1 = hand.pop()
        c2 = hand.pop()
        highest_card = max(c1, c2)
        if highest_card.isFaceCard():
            rank += {'A': 10, 'K': 8, 'Q': 7, 'J': 6}[highest_card.rank]
        else:
            rank += int(highest_card.rank) / 2.0
        gap = abs(c1._rank - c2._rank)
        if not gap:
            rank *= 2
            if rank == 5:
                rank += 1
            if rank < 5:
                rank = 5
        else:
            rank -= {1:1, 2:2, 3:4}.get(gap, 5)

        if highest_card._rank < 'Q': # nie mozna porownywac do Q
            if gap < 2:
                rank += 1

        if c1.suit == c2.suit:
            rank += 2

        return rank

    def hellmuth_tier(self, hand):
        """
        Score by Phil Hellmuth's: "Play Poker Like the Pros"
        """
        if len(hand) != 2:
            return None
        c1 = hand.pop()
        c2 = hand.pop()

    def online_play_expected_value(self, hand):
        """
        Statistics based on real online play
        """
        if len(hand) != 2:
            return None
        c1 = hand.pop()
        c2 = hand.pop()

        ranks = max(c1, c2).rank + min(c1, c2).rank
        if ranks in ['AA', 'KK', 'QQ', 'JJ', 'AKs']:
            return 1, 2.32, 0.78
        if ranks in ['AQs', 'TT', 'AK', 'AJs', 'KQs', '99']:
            return 2, 0.59, 0.38
        if ranks in ['ATs', 'AQ', 'KJs', '88', 'KTs', 'QJs']

#------------------------------------------------------------------------------

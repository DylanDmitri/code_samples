
def getval(card):
    v = card[0]
    if v.isdigit(): return int(v)
    return {'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}[v]

combos = []
class combo:
    def __init__(self, f):
        self.f = eval('lambda hand : ' + f)
        combos.append(self)

    def __call__(self, hand):
        try:
            return self.f(hand)
        except:
            return 0

high_card = combo('max(vals)')
one_pair = combo('max(v for v in hand.groups where hand[v]==2')
two_pair = combo('
three_kind = combo('max(i for i in vals if vals.count(i)==3)')
straight = combo('sorted(vals)[-1] if sorted(vals)==list(range(sorted(hand.vals)[0], sorted(hand.vals)[0]+5)) else 0')
flush = combo('len(set(suites))==1')
full_house = combo('three_kind(hand)*100 + one_pair(hand) if (three_kind(hand) and one_pair(hand)) else 0')
four_of_a_kind = combo('max(i for i in vals if vals.count(i)==4)')
straight_flush = combo('straight(hand) if (straight(hand) and flush(hand)) else 0')

class Hand:
    def __init__(self, cards):
        self.cards = cards
        self.vals = [getval(card) for card in cards]
        self.suites = [card[1] for card in cards]

        self.groups = {i: self.vals.count(i) for i in range(2, 15)}

        self.scores = [combo(self) for combo in combos]
        # self.scores = straight(self)

    def __gt__(self, other):
        return self.scores > other.scores


for line in open('../euler data/poker hands', 'r'):
    cards = line.split()
    p1 = Hand(cards[:5])
    p2 = Hand(cards[5:])

    print('p1=', cards[:5], 'p2=', cards[5:])
    print(p1.scores)
    print(p2.scores)
    print('p1' if p1>p2 else 'p2', 'wins')


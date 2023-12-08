from collections import Counter
from enum import Enum

CARD_POINTS = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
CARD_POINTS_PART_TWO = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']

class HandType(Enum):
    FIVE_OF_A_KIND = [5]
    FOUR_OF_A_KIND = [4, 1]
    FULL_HOUSE = [3, 2]
    THREE_OF_A_KIND = [3, 1, 1]
    TWO_PAIR = [2, 2, 1]
    ONE_PAIR = [2, 1, 1, 1]
    HIGH_CARD = [1, 1, 1, 1, 1]

    def __gt__(self, other):
        if len(self.value) == len(other.value):
            return self.value[0] > other.value[0]
        else:
            return len(self.value) < len(other.value)

    def __eq__(self, other: object) -> bool:
        return self.value == other.value

class Hand:

    def __init__(self, hand: str, bid: int) -> None:
        self.hand: str = hand
        self.bid: int = bid
        self.labels = Counter(hand)
        self.type: HandType = HandType(sorted(self.labels.values(), reverse=True))
        self.card_strength = CARD_POINTS

    def __eq__(self, other):
        return self.type == other.type and self.hand == other.hand

    def __gt__(self, other):
        if self.type == other.type:
            for self_card, other_card in zip(self.hand, other.hand):
                if self_card == other_card:
                    continue
                return self.card_strength.index(self_card) < self.card_strength.index(other_card)
        return self.type > other.type
    
    def __str__(self) -> str:
        return f"{self.hand} ({self.type.name}): {self.bid}"

class HandTwo(Hand):

    def __init__(self, hand: str, bid: int) -> None:
        super().__init__(hand, bid)
        self.card_strength = CARD_POINTS_PART_TWO
        
        self.jokers = self.labels.get('J', 0)
        newType = sorted(self.labels.values(), reverse=True)
        if self.jokers > 0:
            # horrible edge case handling
            if self.jokers == newType[0]:
                if Counter(self.labels.values())[self.jokers] > 1:
                    newType[0] += self.jokers
                    newType.remove(self.jokers)
                elif Counter(self.labels.values())[self.jokers] == 1 and len(newType) > 1:
                    newType[0] += newType[1]
                    newType.remove(newType[1])
            else:
                newType[0] += self.jokers
                newType.remove(self.jokers)
        self.type = HandType(newType)

if __name__ == '__main__':
    with open('input') as reader:
        lines = reader.readlines()
        hands = []
        hands2 = []
        for line in lines:
            hand, bid = line.strip().split(' ')
            hands.append(Hand(hand, int(bid)))
            hands2.append(HandTwo(hand, int(bid)))

        # print("\n".join(f"{str(h)}: {rank + 1}" for rank, h in enumerate(sorted(hands))))
        # print("\n".join(f"{str(h)}: {rank + 1}" for rank, h in enumerate(sorted(hands2))))

        print(f"part one: {sum(h.bid * (i + 1) for i, h in enumerate(sorted(hands)))}")
        print(f"part two: {sum(h.bid * (i + 1) for i, h in enumerate(sorted(hands2)))}")
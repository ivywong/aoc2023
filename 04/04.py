import re

def part_one(lines: list[str]) -> None:
    parts = re.compile(r"(\d+): ([ \d]*) \| ([ \d]*)")
    
    score = 0
    for line in lines:
        res = re.search(parts, line).groups()
        id = int(res[0])
        winning = {int(n.group()) for n in re.finditer('\d+', res[1])}
        chosen = {int(n.group()) for n in re.finditer('\d+', res[2])}
        
        common = len(winning & chosen)
        if common > 0:
            score += 2 ** (common - 1)
    print(score)

def part_two(lines: list[str]) -> None:
    parts = re.compile(r"(\d+): ([ \d]*) \| ([ \d]*)")
    
    cards_by_id = {}
    for line in lines:
        res = re.search(parts, line).groups()
        id = int(res[0])
        winning = {int(n.group()) for n in re.finditer('\d+', res[1])}
        chosen = {int(n.group()) for n in re.finditer('\d+', res[2])}
        cards_by_id[id] = { 'winning': winning, 'chosen': chosen, 'common': len(winning & chosen) }
    
    num_cards = 0
    cards = { i: 1 for i in range(1, len(cards_by_id) + 1)}
    for card in range(1, len(cards) + 1):
        while cards[card] != 0:
            num_cards += 1
            cards[card] -= 1
            for i in range(1, cards_by_id[card]['common'] + 1):
                cards[card + i] += 1
    print(num_cards)

if __name__ == '__main__':
    with open('input') as reader:
        lines = reader.readlines()

        part_one(lines)
        part_two(lines)
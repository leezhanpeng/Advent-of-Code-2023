part1_answer = 0
part2_answer = 0
mapping = {
    "T": "A",
    "J": "B",
    "Q": "C",
    "K": "D",
    "A": "E",
}

def get_value(cards, no_joker):
    card_tracker = {}
    mapped_cards = ""
    for card in cards:
        card = mapping.get(card, card)
        mapped_cards += card
        if card not in card_tracker:
            card_tracker[card] = 1
        else:
            card_tracker[card] += 1
    if no_joker:
        return "".join(map(str, sorted(list(card_tracker.values()), reverse=True))) + mapped_cards
    
    if mapping["J"] in card_tracker:
        j_count = card_tracker[mapping["J"]]
        card_tracker.pop(mapping["J"])
        if card_tracker:
            max_amount = max(card_tracker.values())
            for card in card_tracker:
                if card_tracker[card] == max_amount:
                    card_tracker[card] += j_count
                    break
        else:
            card_tracker["1"] = 5

    mapped_cards = mapped_cards.replace(mapping["J"], "1")
    return "".join(map(str, sorted(list(card_tracker.values()), reverse=True))) + mapped_cards

with open("input.txt") as f:
    bets = []
    for bet in f:
        bets.append(bet.split())
    part1_bets = sorted(bets, key=lambda x: get_value(x[0], True))
    part2_bets = sorted(bets, key=lambda x: get_value(x[0], False))
    for i in range(len(part1_bets)):
        part1_answer += int(part1_bets[i][1]) * (i + 1)
        part2_answer += int(part2_bets[i][1]) * (i + 1)

# Part 1 answer
print(part1_answer)

# Part 2 answer
print(part2_answer)

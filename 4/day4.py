part1_answer = 0
part2_answer = 0

scratch_cards_count = {}
with open("input.txt") as f:
    for card in f:
        card_num, card_vals = card.strip().split(": ")
        card_num = int(card_num.split(" ")[-1])
        if card_num not in scratch_cards_count:
            scratch_cards_count[card_num] = 1
        else:
            scratch_cards_count[card_num] += 1

        winning_nums, nums = card_vals.split(" | ")
        winning_nums = list(map(int, filter(lambda x: x != "", winning_nums.split(" "))))
        nums = list(map(int, filter(lambda x: x != "", nums.split(" "))))
        matching_nums_count = len(set(winning_nums) & set(nums))
        if matching_nums_count != 0:
            part1_answer += 2**(matching_nums_count - 1)

        for i in range(card_num + 1, card_num + 1 + matching_nums_count):
            if i not in scratch_cards_count:
                scratch_cards_count[i] = scratch_cards_count[card_num]
            else:
                scratch_cards_count[i] += scratch_cards_count[card_num]

for card_count in scratch_cards_count.values():
    part2_answer += card_count

# Part 1 answer
print(part1_answer)

# Part 2 answer
print(part2_answer)

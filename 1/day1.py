mapping = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

with open("input.txt") as f:
    part1_total = 0
    part2_total = 0

    for line in f:
        part1_digits = list(filter(lambda x: x.isdigit(), line))
        part1_total += int(part1_digits[0] + part1_digits[-1])

        for number in mapping:
            line = line.replace(number, number[:2] + mapping[number] + number[2:])
        part2_digits = list(filter(lambda x: x.isdigit(), line))
        part2_total += int(part2_digits[0] + part2_digits[-1])

    # Part 1 Answer
    print(part1_total)

    # Part 2 Answer
    print(part2_total)

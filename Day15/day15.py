part1_answer = 0
part2_answer = 0

with open("input.txt") as f:
    seq = f.readline().strip().split(",")

boxes = [[] for _ in range(256)]
lengths = {}
hash_tracker = {}
for step in seq:
    part1_value = 0
    for char in step:
        part1_value += ord(char)
        part1_value *= 17
        part1_value %= 256
    part1_answer += part1_value

    if "=" in step:
        label, length = step.split("=")
        if label in hash_tracker:
            lengths[label] = int(length)
        else:
            hash = 0
            for char in label:
                hash += ord(char)
                hash *= 17
                hash %= 256
            boxes[hash].append(label)
            lengths[label] = int(length)
            hash_tracker[label] = hash
    else:
        label = step[:-1]
        if label in hash_tracker:
            boxes[hash_tracker[label]].remove(label)
            del hash_tracker[label]
            del lengths[label]

for i in range(len(boxes)):
    for j in range(len(boxes[i])):
        part2_answer += (i + 1) * (j + 1) * lengths[boxes[i][j]]

# Part 1 answer
print(part1_answer)

# Part 2 answer
print(part2_answer)

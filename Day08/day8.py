from math import gcd

part1_answer = 0
part2_answer = 1

part1_start = "AAA"
part1_end = "ZZZ"
part2_starts = []

network = {}
with open("input.txt") as f:
    instructions = f.readline().strip()
    f.readline() # skip blank line
    for node in f:
        root, children = node.split(" = ")
        network[root] = (children[1:4], children[6:9])
        if root[-1] == "A":
            part2_starts.append(root)

direction = {"R": 1, "L": 0}
instr_index = 0

part1_location = part1_start
while part1_location != part1_end:
    instruction = instructions[instr_index]
    part1_location = network[part1_location][direction[instruction]]
    part1_answer += 1
    
    instr_index += 1
    instr_index %= len(instructions)

part2_locations = part2_starts
part2_steps = []
for location in part2_locations:
    instr_index = 0
    steps = 0
    while location[-1] != "Z":
        instruction = instructions[instr_index]
        location = network[location][direction[instruction]]
        steps += 1
        
        instr_index += 1
        instr_index %= len(instructions)
    part2_steps.append(steps)

for step in part2_steps:
    part2_answer = part2_answer*step//gcd(part2_answer, step)

# Part 1 answer
print(part1_answer)

# Part 2 answer
print(part2_answer)

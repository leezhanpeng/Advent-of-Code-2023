part1_answer = float('inf')
part2_answer = float('inf')

mappings = [[] for i in range(7)]

with open("input.txt") as f:
    seeds = list(map(int, f.readline().split()[1:])) # get seed
    f.readline() # skip first blank line

    mapping_index = -1
    line = f.readline().strip()
    while True:
        if len(line) == 0 and mapping_index == len(mappings) - 1:
            break
        if line != "":
            if ":" in line:
                mapping_index += 1
            else:
                values = list(map(int, line.split()))
                mappings[mapping_index].append((values[1], values[1] + values[2] - 1, values[0]))
        
        line = f.readline().strip()

for i in range(len(mappings)):
    mappings[i].sort(key=lambda x: x[0])

def get_location(init, amount, index):
    # print(init, amount, index)
    if index == len(mappings):
        return init

    all_locations = []
    mapping = mappings[index]
    mapped = False
    for start, end, next in mapping:
        if init >= start:
            if init > end:
                continue
            
            if init + amount - 1 <= end:
                all_locations.append(get_location(init - start + next, amount, index + 1))
                mapped = True
                break
            else:
                all_locations.append(get_location(init - start + next, end - init + 1, index + 1))
                amount = amount - end + init - 1
                init = end + 1
        else:
            if init + amount - 1 >= start:
                all_locations.append(get_location(next, init + amount - 1 - start, index + 1))
                all_locations.append(get_location(init, start - init, index + 1))
    if not mapped:
        all_locations.append(get_location(init, amount, index + 1))

    return min(all_locations)

for seed in seeds:
    location = get_location(seed, 1, 0)
    if part1_answer > location:
        part1_answer = location

seed_index = 0
while seed_index < len(seeds):
    min_location = get_location(seeds[seed_index], seeds[seed_index + 1], 0)
    if part2_answer > min_location:
        part2_answer = min_location
    seed_index += 2

# Part 1 answer
print(part1_answer)

# Part 2 answer
print(part2_answer)

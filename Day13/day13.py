part1_answer = 0
part2_answer = 0

def find_mirror(pattern, is_part1):
    for i in range(len(pattern) - 1):
        diff = 0
        is_mirror = True
        up_idx = i
        down_idx = i + 1
        while up_idx > -1 and down_idx < len(pattern):
            diff += sum(pattern[up_idx][i] != pattern[down_idx][i] for i in range(len(pattern[up_idx])))
            if diff > 1:
                break

            up_idx -= 1
            down_idx += 1
        
        if (is_part1 and diff == 0) or (not is_part1 and diff == 1):
            return i + 1
    return 0

patterns = [[[],[]]]
with open("input.txt") as f:
    index = 0
    for line in f:
        row = line.strip()
        if row:
            patterns[index][0].append(row)
            if len(patterns[index][1]) == 0:
                for point in row:
                    patterns[index][1].append(point)
            else:
                for i in range(len(patterns[index][1])):
                    patterns[index][1][i] = patterns[index][1][i] + row[i]
        else:
            index += 1
            patterns.append([[],[]])

for pattern in patterns:
    part1_answer += find_mirror(pattern[0], True) * 100 + find_mirror(pattern[1], True)
    part2_answer += find_mirror(pattern[0], False) * 100 + find_mirror(pattern[1], False)

# Part 1 answer
print(part1_answer)

# Part 2 answer
print(part2_answer)

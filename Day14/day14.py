part1_answer = 0
part2_answer = 0

mapping = []
with open("input.txt") as f:
    for line in f:
        mapping.append(line.strip())

memo = {}
memo_inv = {}
cycle_count = 1
while cycle_count < 1000000000:
    for i in range(len(mapping)):
        row = mapping[i]
        for j in range(len(row)):
            piece = row[j]
            if piece == "O":
                drop_to = i
                while drop_to - 1 > -1 and mapping[drop_to - 1][j] == ".":
                    drop_to -= 1
                mapping[i] = mapping[i][:j] + "." + mapping[i][j+1:]
                mapping[drop_to] = mapping[drop_to][:j] + "O" + mapping[drop_to][j+1:]
    if part1_answer == 0:
        for i in range(len(mapping)):
            part1_answer += mapping[i].count("O") * (len(mapping) - i)
    for i in range(len(mapping)):
        row = mapping[i]
        for j in range(len(row)):
            piece = row[j]
            if piece == "O":
                drop_to = j
                while drop_to - 1 > -1 and mapping[i][drop_to - 1] == ".":
                    drop_to -= 1
                mapping[i] = mapping[i][:j] + "." + mapping[i][j+1:]
                mapping[i] = mapping[i][:drop_to] + "O" + mapping[i][drop_to+1:]
    for i in range(len(mapping)-1, -1, -1):
        row = mapping[i]
        for j in range(len(row)):
            piece = row[j]
            if piece == "O":
                drop_to = i
                while drop_to + 1 < len(mapping) and mapping[drop_to + 1][j] == ".":
                    drop_to += 1
                mapping[i] = mapping[i][:j] + "." + mapping[i][j+1:]
                mapping[drop_to] = mapping[drop_to][:j] + "O" + mapping[drop_to][j+1:]
    for i in range(len(mapping)):
        row = mapping[i]
        for j in range(len(row)-1, -1, -1):
            piece = row[j]
            if piece == "O":
                drop_to = j
                while drop_to + 1 < len(row) and mapping[i][drop_to + 1] == ".":
                    drop_to += 1
                mapping[i] = mapping[i][:j] + "." + mapping[i][j+1:]
                mapping[i] = mapping[i][:drop_to] + "O" + mapping[i][drop_to+1:]
    new_mapping = "-".join(mapping)
    if new_mapping not in memo:
        memo[new_mapping] = cycle_count
        memo_inv[cycle_count] = new_mapping
        cycle_count += 1
    else:
        break

final_idx = ((1000000000 - memo["-".join(mapping)]) % (cycle_count - memo["-".join(mapping)])) + memo["-".join(mapping)]
final_mapping = memo_inv[final_idx].split("-")
for i in range(len(final_mapping)):
    part2_answer += final_mapping[i].count("O") * (len(final_mapping) - i)

# Part 1 answer
print(part1_answer)

# Part 2 answer
print(part2_answer)

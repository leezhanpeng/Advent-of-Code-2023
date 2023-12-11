part1_answer = 0
part2_answer = 0

universe = []
galaxies = []
empty_rows = []
empty_cols = []
with open("input.txt") as f:
    row_count = 0
    for row in f:
        row = row.strip()
        universe.append(row)
        if len(set(row)) == 1:
            empty_rows.append(row_count)
        else:
            galaxies.extend([(row_count, i) for i, char in enumerate(row) if char == "#"])
        row_count += 1

for i in range(len(universe[0])):
    column = [universe[j][i] for j in range(len(universe))]
    if len(set(column)) == 1:
        empty_cols.append(i)

for i in range(len(galaxies) - 1):
    for j in range(i + 1, len(galaxies)):
        galaxy_one, galaxy_two = galaxies[i], galaxies[j]

        for spread in [1, 999999]:
            spreaded_galaxy_one = (galaxy_one[0] + spread*len([x for x in empty_rows if x < galaxy_one[0]]), galaxy_one[1] + spread*len([y for y in empty_cols if y < galaxy_one[1]]))
            spreaded_galaxy_two = (galaxy_two[0] + spread*len([x for x in empty_rows if x < galaxy_two[0]]), galaxy_two[1] + spread*len([y for y in empty_cols if y < galaxy_two[1]]))
            distance = abs(spreaded_galaxy_one[0] - spreaded_galaxy_two[0]) + abs(spreaded_galaxy_one[1] - spreaded_galaxy_two[1])
            if spread == 1:
                part1_answer += distance
            else:
                part2_answer += distance

# Part 1 answer
print(part1_answer)

# Part 2 answer
print(part2_answer)

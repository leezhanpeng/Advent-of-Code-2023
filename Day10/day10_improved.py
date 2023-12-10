part1_answer = 1
part2_answer = 0

UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)
directions = [UP, DOWN, LEFT, RIGHT]

pipes = {
    "|": [UP, DOWN],
    "-": [LEFT, RIGHT],
    "L": [UP, RIGHT],
    "J": [UP, LEFT],
    "7": [DOWN, LEFT],
    "F": [DOWN, RIGHT],
    ".": []
}

largest_x = -1
largest_y = -1

maze = {}
piping = {}
with open("input.txt") as f:
    row_idx = 0
    for tiles in f:
        for i in range(len(tiles.strip())):
            position = (row_idx, i)
            tile = tiles[i]
            largest_x = max(largest_x, position[0])
            largest_y = max(largest_y, position[1])

            if tile == "S":
                start_pos = position
                maze[start_pos] = []
            else:
                maze[position] = pipes[tile]
                piping[position] = tile
        row_idx += 1

branches = []
good_directions = []
for x, y in directions:
    new_pos = (start_pos[0] + x, start_pos[1] + y)
    if new_pos in maze and (x * -1, y * -1) in maze[new_pos]:
        branches.append(new_pos)
        good_directions.append((x, y))
        maze[start_pos].append((x, y))

if UP in good_directions and DOWN in good_directions:
    piping[start_pos] = "|"
elif LEFT in good_directions and RIGHT in good_directions:
    piping[start_pos] = "-"
elif UP in good_directions and LEFT in good_directions:
    piping[start_pos] = "J"
elif UP in good_directions and RIGHT in good_directions:
    piping[start_pos] = "L"
elif DOWN in good_directions and LEFT in good_directions:
    piping[start_pos] = "7"
elif DOWN in good_directions and RIGHT in good_directions:
    piping[start_pos] = "F"

pos_one, pos_two = branches
main_pipe = {start_pos, pos_one, pos_two}

old_pos_one = start_pos
old_pos_two = start_pos
while pos_one != pos_two:
    for x, y in maze[pos_one]:
        if (pos_one[0] + x, pos_one[1] + y) != old_pos_one:
            old_pos_one = pos_one
            pos_one = (pos_one[0] + x, pos_one[1] + y)
            break
    for x, y in maze[pos_two]:
        if (pos_two[0] + x, pos_two[1] + y) != old_pos_two:
            old_pos_two = pos_two
            pos_two = (pos_two[0] + x, pos_two[1] + y)
            break
    main_pipe.add(pos_one)
    main_pipe.add(pos_two)
    part1_answer += 1

for x in range(largest_x + 1):
    for y in range(largest_y + 1):
        if (x, y) in main_pipe:
            continue
        amount = 0
        for i in range(y + 1, largest_y + 1):
            if (x,i) in main_pipe and piping[(x, i)] in ["|", "L", "J"]:
                amount += 1
        if amount % 2 == 1:
            part2_answer += 1

# Part 1 answer
print(part1_answer)

# Part 2 answer
print(part2_answer)

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

side_one_right = True
side_one_top = None
side_one_left = False
side_one_down = None
side_one = set()
side_two = set()

for pipe in main_pipe:
    if UP in maze[pipe] and DOWN in maze[pipe]:
        beginning = pipe
        break

curr_pos = beginning
old_pos = curr_pos
while True:
    if side_one_right == True:
        side_one.add((curr_pos[0] + RIGHT[0], curr_pos[1] + RIGHT[1]))
    elif side_one_right == False:
        side_two.add((curr_pos[0] + RIGHT[0], curr_pos[1] + RIGHT[1]))
    if side_one_left == True:
        side_one.add((curr_pos[0] + LEFT[0], curr_pos[1] + LEFT[1]))
    elif side_one_left == False:
        side_two.add((curr_pos[0] + LEFT[0], curr_pos[1] + LEFT[1]))
    if side_one_down == True:
        side_one.add((curr_pos[0] + DOWN[0], curr_pos[1] + DOWN[1]))
    elif side_one_down == False:
        side_two.add((curr_pos[0] + DOWN[0], curr_pos[1] + DOWN[1]))
    if side_one_top == True:
        side_one.add((curr_pos[0] + UP[0], curr_pos[1] + UP[1]))
    elif side_one_top == False:
        side_two.add((curr_pos[0] + UP[0], curr_pos[1] + UP[1]))

    for x, y in maze[curr_pos]:
        next_pos = (curr_pos[0] + x, curr_pos[1] + y)
        if next_pos != old_pos:
            if piping[curr_pos] == "|":
                if piping[next_pos] == "L":
                    side_one_down = side_one_left
                    side_one_right = None
                elif piping[next_pos] == "J":
                    side_one_down = side_one_right
                    side_one_left = None
                elif piping[next_pos] == "7":
                    side_one_top = side_one_right
                    side_one_left = None
                elif piping[next_pos] == "F":
                    side_one_top = side_one_left
                    side_one_right = None

            elif piping[curr_pos] == "-":
                if piping[next_pos] == "L":
                    side_one_left = side_one_down
                    side_one_top = None
                elif piping[next_pos] == "J":
                    side_one_right = side_one_down
                    side_one_top = None
                elif piping[next_pos] == "7":
                    side_one_right = side_one_top
                    side_one_down = None
                elif piping[next_pos] == "F":
                    side_one_left = side_one_top
                    side_one_down = None
                    
            elif piping[curr_pos] == "L":
                if piping[next_pos] == "J":
                    side_one_right = side_one_left
                    side_one_left = None
                elif piping[next_pos] == "7":
                    side_one_right = not side_one_left
                    side_one_top = not side_one_down
                    side_one_left = None
                    side_one_down = None
                elif piping[next_pos] == "F":
                    side_one_top = side_one_down
                    side_one_down = None
                elif piping[next_pos] == "-":
                    side_one_top = not side_one_left
                    side_one_left = None
                elif piping[next_pos] == "|":
                    side_one_right = not side_one_down
                    side_one_down = None
                    
            elif piping[curr_pos] == "J":
                if piping[next_pos] == "7":
                    side_one_top = side_one_down
                    side_one_down = None
                elif piping[next_pos] == "F":
                    side_one_top = not side_one_down
                    side_one_left = not side_one_right
                    side_one_down = None
                    side_one_right = None
                elif piping[next_pos] == "L":
                    side_one_left = side_one_right
                    side_one_right = None
                elif piping[next_pos] == "-":
                    side_one_top = not side_one_right
                    side_one_right = None
                elif piping[next_pos] == "|":
                    side_one_left = not side_one_down
                    side_one_down = None

            elif piping[curr_pos] == "7":
                if piping[next_pos] == "J":
                    side_one_down = side_one_top
                    side_one_top = None
                elif piping[next_pos] == "F":
                    side_one_left = side_one_right
                    side_one_right = None
                elif piping[next_pos] == "L":
                    side_one_down = not side_one_top
                    side_one_left = not side_one_right
                    side_one_top = None
                    side_one_right = None
                elif piping[next_pos] == "-":
                    side_one_down = not side_one_right
                    side_one_right = None
                elif piping[next_pos] == "|":
                    side_one_left = not side_one_top
                    side_one_top = None

            elif piping[curr_pos] == "F":
                if piping[next_pos] == "J":
                    side_one_down = not side_one_top
                    side_one_right = not side_one_left
                    side_one_top = None
                    side_one_left = None
                elif piping[next_pos] == "7":
                    side_one_right = side_one_left
                    side_one_left = None
                elif piping[next_pos] == "L":
                    side_one_down = side_one_top
                    side_one_top = None
                elif piping[next_pos] == "-":
                    side_one_down = not side_one_left
                    side_one_left = None
                elif piping[next_pos] == "|":
                    side_one_right = not side_one_top
                    side_one_top = None
    

            old_pos = curr_pos
            curr_pos = next_pos
            break

    if curr_pos == beginning:
        break

visited_side_one = set()
visited_side_two = set()

side_one_outside = False
while len(side_one) != 0:
    tile = side_one.pop()
    if tile[0] > largest_x or tile[1] > largest_y or tile[0] < 0 or tile[1] < 0:
        side_one_outside = True
        continue
    if tile not in visited_side_one and tile not in main_pipe:
        visited_side_one.add(tile)
        for x, y in directions:
            side_one.add((tile[0] + x, tile[1] + y))

while len(side_two) != 0:
    tile = side_two.pop()
    if tile[0] > largest_x or tile[1] > largest_y or tile[0] < 0 or tile[1] < 0:
        continue
    if tile not in visited_side_two and tile not in main_pipe:
        visited_side_two.add(tile)
        for x, y in directions:
            side_two.add((tile[0] + x, tile[1] + y))

if side_one_outside:
    part2_answer = len(visited_side_two)
else:
    part2_answer = len(visited_side_one)

# Part 1 answer
print(part1_answer)

# Part 2 answer
print(part2_answer)

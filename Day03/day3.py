part1_answer = 0
part2_answer = 0

schema = []
symbols_location = {}
with open("input.txt") as f:
    row_count = 0
    for row in f:
        row = row.strip()
        schema.append(row)
        for i in range(len(row)):
            if not row[i].isdigit() and row[i] != ".":
                symbols_location[(row_count, i)] = (row[i], 0, 1)
        row_count += 1
                
row = 0
col = 0
gears = []
while row < len(schema):
    while col < len(schema[row]):
        is_part = False
        char = schema[row][col]
        start = col
        end = col
        if char.isdigit():
            while end < len(schema[row]) and schema[row][end].isdigit():
                end += 1

            surrounding_coordinates = [(row, start - 1), (row, end)]
            for i in range(start - 1, end + 1):
                surrounding_coordinates.append((row - 1, i))
                surrounding_coordinates.append((row + 1, i))

            for coord in surrounding_coordinates:
                if coord in symbols_location:
                    is_part = True
                    info = symbols_location[coord]
                    symbols_location[coord] = (info[0], info[1] + 1, info[2] * int(schema[row][start:end]))
                        
            if is_part:
                part1_answer += int(schema[row][start:end])
        col = end + 1
        
    col = 0
    row += 1

for symbols in symbols_location:
    if symbols_location[symbols][0] == "*" and symbols_location[symbols][1] == 2:
        part2_answer += symbols_location[symbols][2]

# Part 1 answer
print(part1_answer)

# Part 2 answer
print(part2_answer)

    
            

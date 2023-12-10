col_limit = {
    "red": 12,
    "green": 13,
    "blue": 14
}

with open("input.txt") as f:
    part1_answer = 0
    part2_answer = 0

    for game in f:

        is_possible = True
        smallest_sizes = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        
        game_data = game.split(":")
        draws = game_data[1].split(";")
        
        for draw in draws:
            cols = draw.split(", ")
            for val_col in cols:
                val, colour = val_col.strip().split(" ")
                if col_limit[colour] < int(val):
                    is_possible = False
                if smallest_sizes[colour] < int(val):
                    smallest_sizes[colour] = int(val)
                
        if is_possible:
            part1_answer += int(game_data[0].split(" ")[1])

        power = 1
        for size in smallest_sizes.values():
            power *= size
        part2_answer += power

    # Part 1 answer
    print(part1_answer)

    # Part 2 answer
    print(part2_answer)

    
            

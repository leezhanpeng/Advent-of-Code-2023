import math

def get_ways_count(data):
    time, distance = data
    upper_bound = math.ceil((time + math.sqrt(time**2 - 4*distance)) / 2 - 1)
    lower_bound = math.floor((time - math.sqrt(time**2 - 4*distance)) / 2 + 1)
    return upper_bound - lower_bound + 1

with open("input.txt") as f:
    times = f.readline().split()[1:]
    distances = f.readline().split()[1:]
    time_dist_pair = list(map(lambda x, y: (int(x), int(y)), times, distances))
    part1_answer = math.prod(map(lambda x: get_ways_count(x), time_dist_pair))
    part2_answer = get_ways_count((int("".join(times)), int("".join(distances))))

# Part 1 answer
print(part1_answer)

# Part 2 answer
print(part2_answer)

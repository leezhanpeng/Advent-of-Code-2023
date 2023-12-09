part1_answer = 0
part2_answer = 0

def diff(numbers):
    if set(numbers) == {0}:
        return 0, 0
    next_nums = []
    for i in range(len(numbers) - 1):
        next_nums.append(numbers[i+1] - numbers[i])
    extrap_front, extrap_back = diff(next_nums)
    return numbers[0] - extrap_front, numbers[-1] + extrap_back
    

with open("input.txt") as f:
    for numbers in f:
        front, back = diff(list(map(int, numbers.split())))
        part1_answer += back
        part2_answer += front

# Part 1 answer
print(part1_answer)

# Part 2 answer
print(part2_answer)

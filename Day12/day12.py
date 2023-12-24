part1_answer = 0
part2_answer = 0

def combinations(row, cond, cond_idx, prev=None, memo={}):
    if row == "":
        if sum(cond) != 0:
            return 0
        return 1
    
    if (row, tuple(cond), cond_idx, prev) in memo:
        return memo[(row, tuple(cond), cond_idx, prev)]

    result = 0

    if row[0] == ".":
        if prev == None or prev == "." or cond[cond_idx] == 0:
            result += combinations(row[1:], cond, cond_idx, prev if prev == None else ".", memo)

    if row[0] == "#":
        if prev == ".":
            cond_idx += 1
        if len(cond) != cond_idx:
            if cond[cond_idx] != 0:
                cond[cond_idx] -= 1
                result += combinations(row[1:], cond, cond_idx, "#", memo)
                cond[cond_idx] += 1

    if row[0] == "?":  
        if prev == ".":
            cond_idx += 1
        if len(cond) != cond_idx:
            if cond[cond_idx] != 0:
                cond[cond_idx] -= 1
                result += combinations(row[1:], cond, cond_idx, "#", memo)
                cond[cond_idx] += 1
        if prev == ".":
            cond_idx -= 1

        if prev == None or cond[cond_idx] == 0:
            result += combinations(row[1:], cond, cond_idx, prev if prev == None else ".", memo)
    
    memo[(row, tuple(cond), cond_idx, prev)] = result
    return result

with open("input.txt") as f:
    for line in f:
        row, cond = line.strip().split()
        cond = list(map(int, cond.split(",")))
        part1_answer += combinations(row, cond, 0)
        part2_answer += combinations("?".join([row] * 5), cond * 5, 0)

# Part 1 answer
print(part1_answer)

# Part 2 answer
print(part2_answer)

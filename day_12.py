from functools import cache

TEST = False
in_file = "./resources/day_12_test.txt" if TEST else "./resources/day_12_input.txt"


def file_lines():
    with open(in_file) as file:
        for line in file:
            """Custom iteration logic goes here"""
            line = line.strip()
            line = line.split()
            stack, blocks = line
            yield stack, tuple(int(j) for j in blocks.split(","))


def question_1():
    """Answer to the first question of the day"""
    answer = 0
    for true_string, blocks in file_lines():
        length = len(true_string)
        block_length = sum(blocks)
        divisions = len(blocks) + 1
        float = length - (block_length + len(blocks) - 1)

        combos = find_combinations(divisions, float)

        blocks = blocks + (0,)
        for combo in combos:
            sample_string = "".join(["." * (gap + 1) + "#" * block for gap, block in zip(combo, blocks)])[1:-1]
            valid = check_valid(sample_string, true_string)
            print(sample_string, valid)
            if check_valid(sample_string, true_string):
                answer += 1

    return answer


def check_valid(sample_string, true_string):
    for sample_char, true_char in zip(sample_string, true_string):
        if true_char == "?":
            continue
        if true_char != sample_char:
            return False
    return True


def find_combinations(x, float, current_combination=[]):
    if x == 0 and float == 0:
        return [current_combination]
    if x == 0 or float < 0:
        return []

    combinations = []
    for i in range(float + 1):
        combinations += find_combinations(x - 1, float - i, current_combination + [i])

    return combinations


def question_2():
    """Answer to the second question of the day"""
    answer = 0
    for true_string, blocks in file_lines():
        true_string = "?".join([true_string for i in range(5)])
        blocks = 5*blocks
        valid_positions = recersolve(true_string, blocks, 0)
        answer += valid_positions

    return answer


def f(x):
    if x[0] == 1:
        return x[1:]
    return tuple([x[0]-1] + [i for i in x[1:]])


@cache
def recersolve(true_string, blocks, placing):
    # place tiles one square at time
    # base cases
    # run out of blocks
    if len(blocks) == 0:
        return 0 if "#" in true_string else 1

    # run out of space
    if len(true_string) == 0:
        return 0 if sum(blocks) else 1
    # must place tile but can't
    if true_string[0] == "." and placing == 1:
        return 0
    # can't place a tile but must
    if true_string[0] == "#" and placing == -1:
        return 0

    # in the buffer so chose to place and not to place
    if placing == -1:
        return recersolve(true_string[1:], blocks, 0)

    if placing == 0:
        if true_string[0] == ".":
            return recersolve(true_string[1:], blocks, 0)

        placing = 1
        if blocks[0] == 1:
            placing = -1

        if true_string[0] == "#":
            return recersolve(true_string[1:], f(blocks), placing)
        if true_string[0] == "?":
            return recersolve(true_string[1:], f(blocks), placing) + recersolve(true_string[1:], blocks, 0)
    # finish block and go to buffer:
    if placing == 1:
        if blocks[0] == 1:
            return recersolve(true_string[1:], f(blocks), -1)
        # shrink block and go to next
        else:
            return recersolve(true_string[1:], f(blocks), 1)


if __name__ == '__main__':
    answer_1 = question_1()
    print(f"Question 1 answer is: {answer_1}")

    answer_2 = question_2()
    print(f"Question 2 answer is: {answer_2}")

TEST = False
in_file = "./resources/day_5_test.txt" if TEST else "./resources/day_5_input.txt"

def question_1(lines):
    """Answer to the first question of the day"""
    lines = lines.splitlines()
    seeds = lines[0].split(":")[1].split()

    maps = []

    seed_map = {}
    for line in lines[2:]:
        if line == "":
            maps.append(seed_map)
            seed_map = {}
        else:
            vals = line.split()
            seed_map[(int(vals[1]), int(vals[1]) + int(vals[2]))] = (int(vals[0]), int(vals[0]) + int(vals[2]))

    outputs = []
    for seed in seeds:
        seed = transform_seed(seed, maps)
        outputs.append(seed)

    return min(outputs)


def transform_seed(seed, maps):
    for seed_map in maps:
        for seed_range in seed_map:
            if int(seed) in range(*seed_range):
                seed = seed_map[seed_range][0] + int(seed) - seed_range[0]
                break
    return seed


def question_2(lines):
    """Answer to the second question of the day"""

    """Answer to the first question of the day"""
    lines = lines.splitlines()
    seeds_ranges = lines[0].split(":")[1].split()

    seeds_ranges = [(int(seeds_ranges[i]), int(seeds_ranges[i + 1])) for i in range(0, len(seeds_ranges), 2)]

    maps = []
    seed_map = {}
    for line in lines[2:]:
        if line == "":
            maps.append(seed_map)
            seed_map = {}
        else:
            vals = line.split()
            seed_map[(int(vals[1]), int(vals[1]) + int(vals[2]))] = (int(vals[0]), int(vals[0]) + int(vals[2]))

    outputs = []
    for start, step in seeds_ranges:
        seed = start
        while seed < start + step:
            output, x = transform_seed_find_x(seed, maps)
            seed += x
            outputs.append(output)

    return min(outputs)


def transform_seed_find_x(seed, maps):
    seed = int(seed)
    x_min = 1000000000000
    for seed_map in maps:
        for seed_range in seed_map:
            if seed in range(*seed_range):
                x = seed_range[1] - seed
                if x < x_min:
                    x_min = x
                seed = seed_map[seed_range][0] + int(seed) - seed_range[0]
                break
    return seed, x_min


if __name__ == '__main__':
    with open(in_file) as data:
        answer = question_1(data.read())
        print(answer)

    with open(in_file) as data:
        answer = question_2(data.read())
        print(answer)

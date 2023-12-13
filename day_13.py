TEST = False
in_file = "./resources/day_13_test.txt" if TEST else "./resources/day_13_input.txt"

import numpy as np

def file_lines():
    with open(in_file) as file:
        for line in file:
            """Custom iteration logic goes here"""
            line = line.strip()
            line = [i for i in line]
            yield line


def construct_patterns():
    patterns = []
    pattern = []
    for line in file_lines():
        if line:
            pattern.append(line)
        else:
            patterns.append(np.array(pattern))
            pattern = []
    patterns.append(np.array(pattern))

    return patterns

def question_1():
    """Answer to the first question of the day"""
    answer = None
    patterns = construct_patterns()
    reflection_points = 0

    # print(patterns)
    for pattern in patterns:
        reflection_points += 100 * find_reflections(pattern)
        reflection_points += find_reflections(pattern.transpose())

    return answer


def find_reflections(pattern):
    reflection_points = 0
    for i, row in enumerate(pattern[:-1]):
        if (pattern[i] == pattern[i+1]).all():
            # potential reflection
            reflection = True
            ub = i
            lb = i+1
            while ub >= 0 and lb < len(pattern):
                if not (pattern[ub] == pattern[lb]).all():
                    reflection = False
                ub -= 1
                lb += 1
            if reflection:
                print(reflection)
                reflection_points += i+1

    return reflection_points


def question_2():
    """Answer to the second question of the day"""
    patterns = construct_patterns()
    reflection_points = 0

    for pattern in patterns:
        reflection_points += 100 * find_smudge(pattern)
        reflection_points += find_smudge(pattern.transpose())

    return reflection_points


def find_smudge(pattern):
    reflection_points = 0
    for i, row in enumerate(pattern[:-1]):
        if (pattern[i] == pattern[i+1]).all():
            # potential reflection
            reflection = True
            smudge = False
            ub = i
            lb = i+1
            while ub >= 0 and lb < len(pattern):
                if not (pattern[ub] == pattern[lb]).all():
                    # print(np.unique((pattern[ub] == pattern[lb]), return_counts=True))
                    unique, counts = np.unique((pattern[ub] == pattern[lb]), return_counts=True)
                    if dict(zip(unique, counts))[False] == 1:
                        smudge = True
                    else:
                        reflection = False
                        smudge = False
                ub -= 1
                lb += 1
            if reflection and smudge:
                reflection_points += i+1

        if np.unique((pattern[i] == pattern[i+1]), return_counts=True)[1][0] == 1:
            reflection = True
            if i == 0 or i+1 > len(pattern):
                reflection_points += i + 1
            else:
                ub = i-1
                lb = i + 2
                while ub >= 0 and lb < len(pattern):
                    if not (pattern[ub] == pattern[lb]).all():
                        reflection = False
                    ub -= 1
                    lb += 1
                if reflection:
                    reflection_points += i + 1

    return reflection_points


if __name__ == '__main__':
    # answer_1 = question_1()
    # print(f"Question 1 answer is: {answer_1}")

    answer_2 = question_2()
    print(f"Question 2 answer is: {answer_2}")

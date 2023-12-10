TEST = False
in_file = "./resources/day_9_test.txt" if TEST else "./resources/day_9_input.txt"


def file_lines():
    with open(in_file) as file:
        for line in file:
            """Custom iteration logic goes here"""
            line = line.strip()
            line = line.split()
            yield [int(i) for i in line]


def question_1():
    """Answer to the first question of the day"""
    answer = 0
    for line in file_lines():
        intervals = find_intervals(line)
        intervals.reverse()
        intervals.append(line)

        for i, inter in enumerate(intervals[1:]):
            inter.append(inter[-1] + intervals[i][-1])

        answer += intervals[-1][-1]

    return answer


def find_intervals(sequence):
    search = True
    intervals = []
    inters = sequence
    while search:
        inters = [v - inters[i] for i, v in enumerate(inters[1:])]
        if set(inters) == {0}:
            search = False
        intervals.append(inters)
    return intervals


def question_2():
    """Answer to the second question of the day"""
    answer = 0
    for line in file_lines():
        intervals = find_intervals(line)
        intervals.reverse()
        intervals.append(line)

        for i, inter in enumerate(intervals[1:]):
            inter.insert(0, inter[0] - intervals[i][0])

        answer += intervals[-1][0]

    return answer


if __name__ == '__main__':
    answer_1 = question_1()
    print(f"Question 1 answer is: {answer_1}")

    answer_2 = question_2()
    print(f"Question 2 answer is: {answer_2}")

TEST = False
in_file = "./resources/day_19_test.txt" if TEST else "./resources/day_19_input.txt"

from copy import deepcopy as copy

def file_lines():
    with open(in_file) as file:
        """Custom iteration logic goes here"""
        rules = {}
        items = []
        lines = []
        for line in file:
            lines.append(line)

        index = 0
        for line in lines:
            index += 1
            if line == "\n":
                break
            line = line.strip().strip("}")
            name, line = line.split("{")
            line = line.split(",")
            line = [i.split(":") for i in line]
            line[-1] = ["defalt", *line[-1]]
            line = {k: v for (k, v) in line}
            rules[name] = line

        for line in lines[index:]:
            line = line.strip().strip("{").strip("}").split(",")
            line = [i.split("=") for i in line]
            line = {k:v for (k,v) in line}
            items.append(line)

        return rules, items

def question_1():
    """Answer to the first question of the day"""
    answer = 0
    rules, items = file_lines()
    for item in items:
        answer += check_item(rules, item)

    return answer


def evaluate_check(check, item):
    if check == "defalt":
        return True

    letter = check[0]
    symbol = check[1]
    value = check[2:]

    if symbol == "<" and int(item[letter]) < int(value):
        return True

    if symbol == ">" and int(item[letter]) > int(value):
        return True


def check_item(rules, item):
    rule = rules["in"]
    while True:
        for check in rule.keys():
            if evaluate_check(check, item):
                next_rule = rule[check]
                if next_rule == "A":
                    return sum([int(i) for i in item.values()])
                if next_rule == "R":
                    return 0
                rule = rules[next_rule]
                break


def question_2():
    """Answer to the second question of the day"""
    answer = None
    rules, _ = file_lines()

    # recursive solution that takes a dict
    max_val = 4000
    min_val = 0
    answer = recursolve(dict(x=[min_val, max_val], m=[min_val, max_val], a=[min_val, max_val], s=[min_val, max_val]), rules, rules["in"])

    return answer


def recursolve(ranges, rules, rule):
    answer = 0
    for check in rule.keys():
        inner_ranges = copy(ranges)
        if check != "defalt":
            inner_ranges, ranges = augment_ranges(inner_ranges, check)

        if contains_negative(inner_ranges):
            continue

        if rule[check] == "R":
            pass
        elif rule[check] == "A":
            commbinations = 1
            for range in [int(r2) - int(r1) for r1, r2 in inner_ranges.values()]:
                commbinations *= range
            answer += commbinations
        else:
            answer += recursolve(inner_ranges, rules, rules[rule[check]])

    return answer


def augment_ranges(ranges, check):
    outer_ranges = copy(ranges)
    letter = check[0]
    symbol = check[1]
    value = int(check[2:])

    # augment ranges
    if symbol == "<":
        ranges[letter][1] = value-1
        outer_ranges[letter][0] = value-1

    if symbol == ">":
        ranges[letter][0] = value
        outer_ranges[letter][1] = value

    return ranges, outer_ranges

def contains_negative(ranges):
    for r1, r2 in ranges.values():
        if int(r2) <= int(r1):
            return True


if __name__ == '__main__':
    answer_1 = question_1()
    print(f"Question 1 answer is: {answer_1}")

    answer_2 = question_2()
    print(f"Question 2 answer is: {answer_2}")

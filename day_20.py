TEST = False
in_file = "./resources/day_20_test.txt" if TEST else "./resources/day_20_input.txt"

from math import lcm

execution_queue = []

class module:
    def __init__(self, name, targets):
        self.name = name
        self.targets = targets


class Broadcaster(module):

    def receive_pulse(self, sender, level):
        return "L", self.targets


class Flip_flop(module):
    state = False

    def receive_pulse(self, sender, level):
        if level == "L":
            if not self.state:
                self.state = True
                return "H", self.targets
            elif self.state:
                self.state = False
                return "L", self.targets
        else:
            return "L", []



class Conjunction(module):
    state = False
    def __init__(self, name, targets):
        super().__init__(name, targets)
        self.mem = {}

    def add_to_mem(self, sender):
        self.mem[sender] = "L"

    def receive_pulse(self, sender, level):
        self.mem[sender] = level
        if set(self.mem.values()) == {"H"}:
            self.state = True
            return "L", self.targets
        else:
            self.state = False
            return "H", self.targets


with open(in_file) as file:
    modules = {}
    for line in file:
        """Custom iteration logic goes here"""
        line = line.strip()
        module, targets = line.split(" -> ")
        if module[0] == "%":
            modules[module[1:]] = Flip_flop(module[1:], targets.split(", "))
        elif module[0] == "&":
            modules[module[1:]] = Conjunction(module[1:], targets.split(", "))
        else:
            modules[module] = Broadcaster(module, targets.split(", "))

    for module in modules:
        for target in modules[module].targets:
            if isinstance(modules.get(target), Conjunction):
                modules[target].add_to_mem(module)


def question_1():
    """Answer to the first question of the day"""
    lp = 0
    hp = 0

    for button in range(1000):
        execution_queue = [("button", "broadcaster", "L")]
        lp += 1
        while execution_queue:
            sender, module, level = execution_queue.pop(0)
            level, targets = modules[module].receive_pulse(sender, level)

            for target in targets:
                print(f"{module} -{level}-> {target}")
                if level == "L":
                    lp += 1
                else:
                    hp += 1

                if target in modules:
                    execution_queue.append((module, target, level))

    answer = lp*hp
    return answer


def question_2():
    """Answer to the second question of the day"""
    # the input is set up in such a way that there are 4 "tracks" each track needs to send an L signal at the same time
    # the LCM of all tracks will give the answer
    tracks = [0, 0, 0, 0]
    tracks_found = 0
    presses = 0
    while True:
        presses += 1
        execution_queue = [("button", "broadcaster", "L")]
        while execution_queue:
            sender, module, level = execution_queue.pop(0)
            level, targets = modules[module].receive_pulse(sender, level)

            for target in targets:
                # I have modified the labels in my input, it won't work generally
                if module in ["mid1", "mid2", "mid3", "mid4"] and target in ["bot1", "bot2", "bot3", "bot4"] and level == "L":
                    print(f"{module} -{level}-> {target} at presses {presses}")
                    tracks[tracks_found] = presses
                    tracks_found += 1
                    if tracks_found == 4:
                        return lcm(*tracks)

                if target == "rx" and level == "L":
                    return


                if target in modules:
                    execution_queue.append((module, target, level))


if __name__ == '__main__':
    answer_1 = question_1()
    print(f"Question 1 answer is: {answer_1}")

    answer_2 = question_2()
    print(f"Question 2 answer is: {answer_2}")

import re


class NewRulesInt:
    def __init__(self, value):
        self.v = value

    def __add__(self, other):
        return NewRulesInt(self.v + other.v)

    def __sub__(self, other):
        return NewRulesInt(self.v * other.v)


def evaluate(exp):
    return eval(re.sub(r'\d+', lambda m: f'NewRulesInt({m.group(0)})', re.sub(r'\*', '-', exp))).v


def find_expressions_sum(expressions):
    return sum(evaluate(expression) for expression in expressions)


if __name__ == "__main__":
    with open('day18/input.txt') as inp:
        math_expressions = inp.readlines()

    print(find_expressions_sum(math_expressions))  # 24650385570008

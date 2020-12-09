class Interpreter:
    def __init__(self):
        self.accumulator = 0
        self.inst_index = 0
        self.instructions = []
        self.operations = {
            'acc': self.acc,
            'jmp': self.jmp,
            'nop': self.nop
        }

    def is_inst_index_valid(self):
        return 0 <= self.inst_index < len(self.instructions)

    def execute_instruction(self):
        if not self.is_inst_index_valid():
            return False
        instruction = self.instructions[self.inst_index]
        self.operations[instruction[0]](instruction[1])
        return True

    def acc(self, value):
        self.accumulator += value
        self.inst_index += 1

    def jmp(self, value):
        self.inst_index += value

    def nop(self, value):
        self.inst_index += 1

    def prepare_before_process(self, instructions):
        self.accumulator = 0
        self.inst_index = 0
        self.instructions = instructions

    def launch_process(self, instructions):
        self.prepare_before_process(instructions)
        while self.execute_instruction():
            yield self.accumulator, self.inst_index
        return None

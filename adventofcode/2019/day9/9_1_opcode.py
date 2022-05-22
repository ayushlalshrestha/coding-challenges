
def read_from_file(file_path="input.txt"):
    result = list()
    with open(file_path) as fh:
        lines = fh.read().split('\n')
        for line in lines:
            result.extend([int(num) for num in line.split(',')])
    return result


def parse_opcode(instruction):
    foprc = f"{instruction:05}"
    mode2, mode1, mode0 = foprc[:3]
    op = foprc[3:]

    return [int(mode0), int(mode1), int(mode2), int(op)]


class Computer:
    def __init__(self, data):
        self.idx = 0
        self.relative_base = 0
        self.data = data
        self.done = False
        self.output = None
        self.inputs = []

    def get_params(self, mode1, mode2):
        return self.get_param(mode1, 1), self.get_param(mode2, 2)

    def get_param(self, mode, increment):
        val = self.data[self.idx + increment]
        if mode == 0:
            return self.data[val]
        if mode == 2:
            return self.data[val + self.relative_base]
        return val

    def get_output_address(self, mode, increment):
        val = self.data[self.idx + increment]
        if mode == 0:
            pass
        if mode == 2:
            val += self.relative_base
        return val

    def add(self, param1, param2):
        return param1 + param2

    def multiply(self, param1, param2):
        return param1 * param2

    def less_than(self, param1, param2):
        return 1 if param1 < param2 else 0

    def equals(self, param1, param2):
        return 1 if param1 == param2 else 0

    def jump_if_true(self, mode1, mode2):
        param1, param2 = self.get_params(mode1, mode2)
        return param2 if param1 != 0 else self.idx + 3

    def jump_if_false(self, mode1, mode2):
        param1, param2 = self.get_params(mode1, mode2)
        return param2 if param1 == 0 else self.idx + 3

    def calculate(self, input_val):
        self.inputs.append(input_val)
        while True:
            mode1, mode2, mode3, opcode = parse_opcode(self.data[self.idx])
            if opcode == 1:
                param1, param2 = self.get_params(mode1, mode2)
                out_address = self.get_output_address(mode3, 3)
                self.data[out_address] = self.add(param1, param2)
                self.idx += 4
            elif opcode == 2:
                param1, param2 = self.get_params(mode1, mode2)
                out_address = self.get_output_address(mode3, 3)
                self.data[out_address] = self.multiply(param1, param2)
                self.idx += 4
            elif opcode == 3:
                out_address = self.get_output_address(mode1, 1)
                self.data[out_address] = self.inputs.pop(0)
                self.idx += 2
            elif opcode == 4:
                self.output = self.get_param(mode1, 1)
                print(self.output)
                self.idx += 2
                # return self.output
            elif opcode == 5:
                self.idx = self.jump_if_true(mode1, mode2)
            elif opcode == 6:
                self.idx = self.jump_if_false(mode1, mode2)
            elif opcode == 7:
                param1, param2 = self.get_params(mode1, mode2)
                out_address = self.get_output_address(mode3, 3)
                self.data[out_address] = self.less_than(param1, param2)
                self.idx += 4
            elif opcode == 8:
                param1, param2 = self.get_params(mode1, mode2)
                out_address = self.get_output_address(mode3, 3)
                self.data[out_address] = self.equals(param1, param2)
                self.idx += 4
            elif opcode == 9:
                self.relative_base += self.get_param(mode1, 1)
                self.idx += 2
            elif opcode == 99:
                self.done = True
                return self.output


inputseq = read_from_file("/Users/ayushshrestha/my_projects/codeadvent2019/day9/input.txt")
# inputseq = [1102,34463338,34463338,63,1007,63,34463338,63,1005,63,53,1101,0,3,1000,109,988,209,12,9,1000,209,6,209,3,203,0,1008,1000,1,63,1005,63,65,1008,1000,2,63,1005,63,902,1008,1000,0,63,1005,63,58,4,25,104,0,99,4,0,104,0,99,4,17,104,0,99,0,0,1102,32,1,1019,1101,0,500,1023,1101,0,636,1025,1102,36,1,1010,1101,0,29,1013,1102,864,1,1029,1102,21,1,1000,1102,1,507,1022,1102,1,28,1011,1102,38,1,1008,1101,0,35,1004,1101,25,0,1018,1102,24,1,1005,1102,30,1,1009,1102,1,869,1028,1101,0,37,1007,1102,1,23,1017,1102,1,20,1015,1102,1,22,1003,1101,0,39,1001,1102,1,31,1012,1101,701,0,1026,1101,0,641,1024,1101,0,34,1016,1102,1,0,1020,1102,698,1,1027,1102,33,1,1002,1102,26,1,1006,1101,0,1,1021,1101,0,27,1014,109,12,21101,40,0,0,1008,1012,40,63,1005,63,203,4,187,1105,1,207,1001,64,1,64,1002,64,2,64,109,-11,1207,7,37,63,1005,63,223,1105,1,229,4,213,1001,64,1,64,1002,64,2,64,109,14,1206,5,247,4,235,1001,64,1,64,1105,1,247,1002,64,2,64,109,-2,1207,-4,31,63,1005,63,269,4,253,1001,64,1,64,1105,1,269,1002,64,2,64,109,-6,1208,-5,35,63,1005,63,289,1001,64,1,64,1106,0,291,4,275,1002,64,2,64,109,9,21108,41,39,-1,1005,1015,311,1001,64,1,64,1105,1,313,4,297,1002,64,2,64,109,-5,2101,0,-9,63,1008,63,33,63,1005,63,339,4,319,1001,64,1,64,1106,0,339,1002,64,2,64,1205,10,351,4,343,1106,0,355,1001,64,1,64,1002,64,2,64,109,-18,2108,35,9,63,1005,63,375,1001,64,1,64,1105,1,377,4,361,1002,64,2,64,109,18,1205,9,389,1105,1,395,4,383,1001,64,1,64,1002,64,2,64,109,7,21107,42,41,-8,1005,1010,415,1001,64,1,64,1106,0,417,4,401,1002,64,2,64,109,-12,2102,1,0,63,1008,63,29,63,1005,63,437,1106,0,443,4,423,1001,64,1,64,1002,64,2,64,109,3,1208,0,30,63,1005,63,461,4,449,1105,1,465,1001,64,1,64,1002,64,2,64,109,5,1202,-5,1,63,1008,63,31,63,1005,63,489,1001,64,1,64,1106,0,491,4,471,1002,64,2,64,109,15,2105,1,-6,1001,64,1,64,1106,0,509,4,497,1002,64,2,64,109,-10,1206,2,525,1001,64,1,64,1106,0,527,4,515,1002,64,2,64,109,-18,1202,0,1,63,1008,63,39,63,1005,63,553,4,533,1001,64,1,64,1106,0,553,1002,64,2,64,109,1,2107,21,1,63,1005,63,571,4,559,1105,1,575,1001,64,1,64,1002,64,2,64,109,7,2102,1,-8,63,1008,63,39,63,1005,63,601,4,581,1001,64,1,64,1105,1,601,1002,64,2,64,109,2,1201,-7,0,63,1008,63,35,63,1005,63,623,4,607,1106,0,627,1001,64,1,64,1002,64,2,64,109,20,2105,1,-7,4,633,1106,0,645,1001,64,1,64,1002,64,2,64,109,-16,21107,43,44,-4,1005,1011,663,4,651,1105,1,667,1001,64,1,64,1002,64,2,64,109,-11,2107,36,0,63,1005,63,687,1001,64,1,64,1106,0,689,4,673,1002,64,2,64,109,19,2106,0,4,1106,0,707,4,695,1001,64,1,64,1002,64,2,64,109,-14,21108,44,44,6,1005,1015,725,4,713,1105,1,729,1001,64,1,64,1002,64,2,64,109,1,1201,-6,0,63,1008,63,36,63,1005,63,749,1106,0,755,4,735,1001,64,1,64,1002,64,2,64,109,-1,21101,45,0,10,1008,1019,42,63,1005,63,775,1105,1,781,4,761,1001,64,1,64,1002,64,2,64,109,16,21102,46,1,-7,1008,1018,44,63,1005,63,801,1105,1,807,4,787,1001,64,1,64,1002,64,2,64,109,-3,21102,47,1,-4,1008,1018,47,63,1005,63,833,4,813,1001,64,1,64,1105,1,833,1002,64,2,64,109,-14,2108,38,0,63,1005,63,851,4,839,1105,1,855,1001,64,1,64,1002,64,2,64,109,17,2106,0,3,4,861,1106,0,873,1001,64,1,64,1002,64,2,64,109,-31,2101,0,10,63,1008,63,36,63,1005,63,897,1001,64,1,64,1106,0,899,4,879,4,64,99,21101,0,27,1,21101,0,913,0,1106,0,920,21201,1,53612,1,204,1,99,109,3,1207,-2,3,63,1005,63,962,21201,-2,-1,1,21102,940,1,0,1106,0,920,21202,1,1,-1,21201,-2,-3,1,21101,955,0,0,1106,0,920,22201,1,-1,-2,1105,1,966,21201,-2,0,-2,109,-3,2106,0,0]


seq = {}
for i, j in enumerate(inputseq):
    seq.update({i: j})

computer = Computer(seq)
computer.calculate(2)
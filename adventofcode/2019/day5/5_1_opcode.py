#!/usr/local/bin/python3

from functools import reduce

path = "/Users/ayushshrestha/my_projects/codeadvent2019/input"


def read_from_file(file_path):
    with open(file_path, "r") as fh:
        return [int(num) for num in fh.read().split(",")]


def add(lst, *args):
    args = list(args)
    output_pointer = args[-1]
    del args[-1]
    lst[output_pointer] = sum(args)


def multiply(lst, *args):
    args = list(args)
    output_pointer = args[-1]
    del args[-1]
    lst[output_pointer] = reduce(lambda x, y: x * y, args)


def place_to_address(lst, *args):
    args = list(args)
    output_pointer = args[-1]
    del args[-1]
    num = input("Enter your input")
    lst[output_pointer] = int(num)


def output_number(lst, *args):
    args = list(args)
    output_pointer = args[-1]
    del args[-1]
    print("Outputting: {}".format(lst[output_pointer]))


ops = {
    1: {"func": add, "parameters": 3},
    2: {"func": multiply, "parameters": 3},
    3: {"func": place_to_address, "parameters": 1},
    4: {"func": output_number, "parameters": 1},
    99: {"func": None},
}


def convert_list(lst, n):
    opcode, modes = parse_opcode(lst[n])
    func = ops.get(opcode, {}).get("func", None)
    no_parameters = ops.get(opcode, {}).get("parameters")
    if not func:
        return

    inputs = []
    for i in range(no_parameters):
        pointer = lst[n + 1 + i]
        if i + 1 == no_parameters:
            pointer = lst[n + 1 + i]
        elif modes[i] == 0:
            pointer = lst[pointer]
        elif modes[i] == 1:
            pass
        inputs.append(pointer)
    
    func(lst, *inputs)
    return n + 1 + no_parameters


def get_last_n_digit(number, n=1):
    return int(number % 10 ** n)


def parse_opcode(number):
    opcode = get_last_n_digit(number, 2)
    number = (number - opcode) / (10 ** 2)

    mode1 = get_last_n_digit(number)
    number = (number - mode1) / 10

    mode2 = get_last_n_digit(number)
    number = (number - mode2) / 10

    mode3 = get_last_n_digit(number)

    return opcode, [mode1, mode2, mode3]


# intseq = read_from_file(path)
inputseq = [3,225,1,225,6,6,1100,1,238,225,104,0,1,191,196,224,1001,224,-85,224,4,224,1002,223,8,223,1001,224,4,224,1,223,224,223,1101,45,50,225,1102,61,82,225,101,44,39,224,101,-105,224,224,4,224,102,8,223,223,101,5,224,224,1,224,223,223,102,14,187,224,101,-784,224,224,4,224,102,8,223,223,101,7,224,224,1,224,223,223,1001,184,31,224,1001,224,-118,224,4,224,102,8,223,223,1001,224,2,224,1,223,224,223,1102,91,18,225,2,35,110,224,101,-810,224,224,4,224,102,8,223,223,101,3,224,224,1,223,224,223,1101,76,71,224,1001,224,-147,224,4,224,102,8,223,223,101,2,224,224,1,224,223,223,1101,7,16,225,1102,71,76,224,101,-5396,224,224,4,224,1002,223,8,223,101,5,224,224,1,224,223,223,1101,72,87,225,1101,56,77,225,1102,70,31,225,1102,29,15,225,1002,158,14,224,1001,224,-224,224,4,224,102,8,223,223,101,1,224,224,1,223,224,223,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,1007,226,226,224,1002,223,2,223,1006,224,329,1001,223,1,223,8,226,677,224,1002,223,2,223,1005,224,344,1001,223,1,223,107,226,677,224,1002,223,2,223,1006,224,359,1001,223,1,223,8,677,677,224,1002,223,2,223,1005,224,374,1001,223,1,223,1108,226,226,224,1002,223,2,223,1005,224,389,1001,223,1,223,7,677,226,224,1002,223,2,223,1005,224,404,101,1,223,223,7,226,226,224,102,2,223,223,1006,224,419,1001,223,1,223,1108,226,677,224,102,2,223,223,1005,224,434,1001,223,1,223,1107,226,226,224,1002,223,2,223,1006,224,449,1001,223,1,223,1007,677,677,224,102,2,223,223,1006,224,464,1001,223,1,223,107,226,226,224,1002,223,2,223,1005,224,479,101,1,223,223,1107,677,226,224,1002,223,2,223,1005,224,494,1001,223,1,223,1008,677,677,224,102,2,223,223,1005,224,509,101,1,223,223,107,677,677,224,102,2,223,223,1005,224,524,1001,223,1,223,1108,677,226,224,1002,223,2,223,1005,224,539,1001,223,1,223,7,226,677,224,102,2,223,223,1006,224,554,1001,223,1,223,8,677,226,224,1002,223,2,223,1006,224,569,101,1,223,223,108,226,226,224,1002,223,2,223,1006,224,584,1001,223,1,223,1107,226,677,224,1002,223,2,223,1006,224,599,101,1,223,223,1008,226,226,224,102,2,223,223,1005,224,614,1001,223,1,223,1007,226,677,224,1002,223,2,223,1006,224,629,1001,223,1,223,108,677,226,224,102,2,223,223,1005,224,644,101,1,223,223,1008,226,677,224,1002,223,2,223,1005,224,659,101,1,223,223,108,677,677,224,1002,223,2,223,1006,224,674,1001,223,1,223,4,223,99,226]
# inputseq = [1002,4,3,4,33]
if __name__ == "__main__":
    counter = 0
    while True:
        counter = convert_list(inputseq, counter)
        if counter is None:
            break
# print(inputseq)

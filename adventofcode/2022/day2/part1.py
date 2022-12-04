import os

current_dir = os.path.dirname(os.path.abspath(__file__))

win_hand_map = {
    "A": "Y",
    "B": "Z",
    "C": "X",
}
draw_hand_map = {
    "A": "X",
    "B": "Y",
    "C": "Z",
}

def main():
    total = 0
    input_file_path = os.path.join(current_dir, "input")
    with open(input_file_path, "r") as fh:
        line = fh.readline()
        while line:
            first, second = line.split()
            first = first.strip()
            second = second.strip()

            if second == "X":
                total += 1
            if second == "Y":
                total += 2
            if second == "Z":
                total += 3

            if win_hand_map[first] == second:
                total += 6
            elif draw_hand_map[first] == second:
                total += 3
            line = fh.readline()

    print(total)


if __name__ == "__main__":
    main()

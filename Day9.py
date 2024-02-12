import numpy as np


def Travel(path: list) -> np.ndarray:
    spread = GetTravelSpread(path)
    tail_path = np.zeros([spread[3] - spread[1] + 1, spread[2] - spread[0] + 1])
    head_position = [-spread[0], -spread[1]]
    tail_position = [-spread[0], -spread[1]]
    tail_path[tail_position[1], tail_position[0]] = 1

    for p in path:
        if p[0] == "R":
            head_position[0] += p[1]
            if head_position[0] > tail_position[0] + 1:
                tail_path[head_position[1], tail_position[0] + 1:head_position[0]] = 1
                tail_position[0] = head_position[0] - 1
                tail_position[1] = head_position[1]
        elif p[0] == "L":
            head_position[0] -= p[1]
            if head_position[0] < tail_position[0] - 1:
                tail_path[head_position[1], head_position[0] + 1:tail_position[0]] = 1
                tail_position[0] = head_position[0] + 1
                tail_position[1] = head_position[1]
        elif p[0] == "D":
            head_position[1] += p[1]
            if head_position[1] > tail_position[1] + 1:
                tail_path[tail_position[1] + 1:head_position[1], head_position[0]] = 1
                tail_position[0] = head_position[0]
                tail_position[1] = head_position[1] - 1
        elif p[0] == "U":
            head_position[1] -= p[1]
            if head_position[1] < tail_position[1] - 1:
                tail_path[head_position[1] + 1:tail_position[1], head_position[0]] = 1
                tail_position[0] = head_position[0]
                tail_position[1] = head_position[1] + 1

    return tail_path


def GenericTravel(path: list, rope_length: int) -> np.ndarray:
    spread = GetTravelSpread(path)
    rope = [[-spread[0], -spread[1]] for _ in range(rope_length)]
    tail_path = np.zeros([spread[3] - spread[1] + 1, spread[2] - spread[0] + 1])
    tail_path[rope[-1][1], rope[-1][0]] = 1
    for p in path:
        if p[0] == "R":
            MoveRope()
        elif p[0] == "L":
        elif p[0] == "D":
        elif p[0] == "U":


    return tail_path


def MoveRope()


def GetTravelSpread(path: list) -> list:
    max = [0, 0, 0, 0]
    current = [0, 0]
    for p in path:
        if p[0] == "R":
            current[0] += p[1]
            if current[0] > max[2]:
                max[2] = current[0]
        elif p[0] == "L":
            current[0] -= p[1]
            if current[0] < max[0]:
                max[0] = current[0]
        elif p[0] == "D":
            current[1] += p[1]
            if current[1] > max[3]:
                max[3] = current[1]
        elif p[0] == "U":
            current[1] -= p[1]
            if current[1] < max[1]:
                max[1] = current[1]
        
    return max


f = open("input.txt")
path = []
for line in f.readlines():
    p = line.strip().split(" ")
    path.append([p[0], int(p[1])])

tail_path = Travel(path)
print(np.count_nonzero(tail_path))
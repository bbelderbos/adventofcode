def solution_part1(data: str, marker_length=4):
    for i in range(len(data)):
        start, end = i, i + marker_length
        if len(set(data[start:end])) == marker_length:
            return end
    else:
        raise AssertionError("Data should have start-of-packet marker")

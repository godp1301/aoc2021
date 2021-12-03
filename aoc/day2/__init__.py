def _get_unit(line):
    return int(line.split(' ')[1])


def solve(puzzle, submarine):
    for move in puzzle:
        if 'forward' in move:
            submarine.forward(_get_unit(move))
        elif 'down' in move:
            submarine.down(_get_unit(move))
        elif 'up' in move:
            submarine.up(_get_unit(move))

    return submarine.get_position() * submarine.get_depth()

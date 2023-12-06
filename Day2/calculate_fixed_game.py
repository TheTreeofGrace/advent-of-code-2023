import re

max_colours = {
    "red": 12,
    "green": 13,
    "blue": 14
}

reset_cubes = {
    "red": 0,
    "green": 0,
    "blue": 0
}

class CalcPossible():
    def __init__(self) -> None:
        self.game_cubes = {
            "red": 0,
            "green": 0,
            "blue": 0
        }

    def get_cubes(_, line):
        cubes = re.findall(r"(?!(:))((\d+) (red|blue|green))", line)
        return cubes

    def process_value(self, cubes):
        for cube in cubes:
            self.game_cubes[cube[3]] = self.game_cubes[cube[3]] + int(cube[2])

    def get_game_id(_, line):
        return re.search(r"(?!(Game ))\d+", line).group()

    def calculate_possible(self, line):
        gameID = self.get_game_id(line)
        cubes = self.get_cubes(line)
        self.process_value(cubes)
        for val in max_colours:
            if(max_colours[val] < self.game_cubes[val]):
                return 0
        return int(gameID)
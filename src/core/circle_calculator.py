import math


class CircleCalculator:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._setup()
        return cls._instance

    def _setup(self):
        self.table = [['0'] * 10 for _ in range(10)]

    def set_radius(self, radius):
        if radius < 1:
            raise ValueError("Radius must be at least 1")

        grids_number = (radius * 2 - 1) + 4

        self.table = [['0'] * grids_number for _ in range(grids_number)]

        self._apply_skeleton_tiles(radius)

    def _apply_skeleton_tiles(self, radius):
        center = self._find_center()

        self.table[center][center] = '1'

        if radius == 1:
            return

        for i in range(center - (radius - 1), center + (radius - 1) + 1):
            if self.table[i][center] != '1':
                self.table[i][center] = '2'

            if self.table[center][i] != '1':
                self.table[center][i] = '2'

    def _find_center(self):
        size = len(self.table)
        center = size // 2
        return center

    def print_table(self):
        for col in range(len(self.table)):
            for row in range(len(self.table[col])):
                print(self.table[col][row], end=' ')
            print()


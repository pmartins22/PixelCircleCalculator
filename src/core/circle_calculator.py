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
        self.set_radius(1)
        self.print_table()

    def set_radius(self, radius):
        if radius < 1:
            raise ValueError("Radius must be at least 1")

        grids_number = (radius * 2 - 1) + 4

        self.table = [['0'] * grids_number for _ in range(grids_number)]

        self._apply_skeleton_tiles(radius)
        self._apply_circle_tiles(radius)

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

    def _apply_circle_tiles(self, radius):
        if radius == 1:
            return

        for y in range(len(self.table)):
            for x in range(len(self.table[y])):
                if self._pixel_intercepts_circle(radius, x, y) and self.table[y][x] != '1' and self.table[y][x] != '2':
                    self.table[y][x] = '3'

    def _pixel_intercepts_circle(self, radius, px, py):
        center = self._find_center(as_float=True)
        radius = radius - 1
        # Calculate smaller x distance to center
        px1 = px
        px2 = px + 1

        if px1 <= center <= px2:
            smaller_point_x = center
        else:
            if abs(center - px1) < abs(center - px2):
                smaller_point_x = px1
            else:
                smaller_point_x = px2


        # Calculate smaller y distance to center

        # Translate pixel y to cartesian y
        py1 = center * 2 - py - 1
        py2 = py1 + 1

        if py1 <= center <= py2:
            smaller_point_y = center
        else:
            if abs(center - py1) < abs(center - py2):
                smaller_point_y = py1
            else:
                smaller_point_y = py2

        smaller_dist_to_center = math.dist([center, center], [smaller_point_x, smaller_point_y])

        # Calculate larger x distance to center
        if px1 <= center <= px2:
            larger_point_x = center + 0.5
        else:
            if abs(center - px1) > abs(center - px2):
                larger_point_x = px1
            else:
                larger_point_x = px2

        # Calculate larger y distance to center
        if py1 <= center <= py2:
            larger_point_y = center + 0.5
        else:
            if abs(center - py1) > abs(center - py2):
                larger_point_y = py1
            else:
                larger_point_y = py2

        larger_dist_to_center = math.dist([center, center], [larger_point_x, larger_point_y])

        return smaller_dist_to_center < radius < larger_dist_to_center

    def _find_center(self, as_float=False):
        size = len(self.table)
        if as_float:
            return size / 2
        return size // 2

    def print_table(self):
        for col in range(len(self.table)):
            for row in range(len(self.table[col])):
                print(self.table[col][row], end=' ')
            print()


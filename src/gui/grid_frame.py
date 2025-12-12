from tkinter import ttk

class GridFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.base_pixel_size = 20
        self.pixel_size = 20
        self.grid_size = 10
        self.zoom_level = 1.0

        self.COLOR_GRID_LINE = "#CCCCCC"
        self.COLOR_BACKGROUND = "#FFFFFF"
        self.COLOR_AXIS = "#666666"
        self.COLOR_PIXEL_FILLED = "#000000"


import tkinter as tk
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

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.canvas = tk.Canvas(
            self,
            bg=self.COLOR_BACKGROUND,
            highlightthickness=0
        )
        self.canvas.grid(row=0, column=0, sticky="nsew")


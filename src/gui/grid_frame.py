import tkinter as tk
from tkinter import ttk

from src.core.circle_calculator import CircleCalculator


class GridFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.COLOR_BACKGROUND = "#FFFFFF"
        self.COLOR_GRID_LINE = "#CCCCCC"
        self.COLOR_PIXEL_CIRCLE = "#000000"
        self.COLOR_PIXEL_SKELETON = "#FFB303"
        self.COLOR_PIXEL_CENTER = "#FF4603"

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.canvas = tk.Canvas(
            self,
            bg=self.COLOR_BACKGROUND,
            highlightthickness=0
        )
        self.canvas.place(relx=0.5, rely=0.5, anchor="center")

        self.bind("<Configure>", self._on_resize)

        self.after(100, lambda: self._draw_table(table=CircleCalculator().table))

    def _on_resize(self, event=None):
        self.update_idletasks()

        width = self.winfo_width()
        height = self.winfo_height()

        size = min(width, height)

        if size > 1:
            self.canvas.config(width=size, height=size)
            self._draw_table(table=CircleCalculator().table)

    def _draw_table(self, table=None):
        if table is None:
            table = [['0']*10 for _ in range(10)]

        self.canvas.delete("all")

        self._draw_grid(len(table), len(table[0]))
        self._draw_tiles(table)

    def _draw_grid(self, rows, cols):
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()

        if canvas_width <= 1 or canvas_height <= 1:
            return

        for i in range(cols + 1):
            x = i * (canvas_width / cols)
            self.canvas.create_line(x, 0, x, canvas_height, fill=self.COLOR_GRID_LINE)

        for i in range(rows + 1):
            y = i * (canvas_height / rows)
            self.canvas.create_line(0, y, canvas_width, y, fill=self.COLOR_GRID_LINE)

    def _draw_tiles(self, table):
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()

        rows = len(table)
        cols = len(table[0])

        tile_width = canvas_width / cols
        tile_height = canvas_height / rows

        for y in range(rows):
            for x in range(cols):
                tile_type = table[y][x]
                color = None

                if tile_type == '1':
                    color = self.COLOR_PIXEL_CENTER
                elif tile_type == '2':
                    color = self.COLOR_PIXEL_SKELETON
                elif tile_type == '3':
                    color = self.COLOR_PIXEL_CIRCLE

                if color is not None:
                    x1 = x * tile_width
                    y1 = y * tile_height
                    x2 = x1 + tile_width
                    y2 = y1 + tile_height

                    self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="")
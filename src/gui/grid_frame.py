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
        self.canvas.place(relx=0.5, rely=0.5, anchor="center")

        self.bind("<Configure>", self._on_resize)

    def _on_resize(self, event=None):
        self.update_idletasks()

        width = self.winfo_width()
        height = self.winfo_height()

        size = min(width, height)

        if size > 1:
            self.canvas.config(width=size, height=size)




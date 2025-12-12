import tkinter as tk
from tkinter import ttk

class InputPanel(ttk.Frame):
    def __init__(self, parent, on_calculate_callback):
        super().__init__(parent)

        self.on_calculate = on_calculate_callback

        label = ttk.Label(self, text="Radius:")
        label.grid(row=0, column=0, padx=5)



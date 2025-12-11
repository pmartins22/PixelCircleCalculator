import tkinter as tk
from tkinter import ttk

from src.gui.grid_frame import GridFrame


class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("PixelCircleCalculator")
        self.root.geometry("800x700")

        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        main_frame = ttk.Frame(root, padding="10")
        main_frame.grid(row=0, column=0, sticky=tk.NSEW)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(0, weight=1)



from tkinter import *

from src.core.circle_calculator import CircleCalculator
from src.gui.main_window import *

if __name__ == "__main__":
    CircleCalculator().set_radius(10)

    root = Tk()
    app = MainWindow(root)
    root.mainloop()
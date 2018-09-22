from tkinter import Tk
from UI import HotsCastControllerUI

class HotsCastController:
    def __init__(self):
        self.window = Tk()
        ui = HotsCastControllerUI(self.window)
        ui.load()
        self.window.mainloop()

hcc = HotsCastController()

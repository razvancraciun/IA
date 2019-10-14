import tkinter as tk
from PIL import ImageTk, Image

class ConsoleDisplay:
    def __init__(self):
        pass

    def display(self,states):
        for state in states:
            print(state)

class GuiDisplay:
    def __init__(self):
        pass

    def display(self,states):
        print('gui display not yet implemented')
        window = tk.Tk()
        window.title('Missionaries and Canibals')
        window.geometry('800x800')
        window.resizable(0,0)
        c_img = ImageTk.PhotoImage(Image.open('img/cannibal.png'))
        cannibal = tk.Label(window, image = c_img)
        m_img = ImageTk.PhotoImage(Image.open('img/missionary.png'))
        missionary = tk.Label(window, image = m_img)
        cannibal.place(x=100, y= 100)
        missionary.place(x=200, y= 200)
        window.mainloop()

class Display:
    console = 'console'
    gui = 'gui'

    def object(string):
        if string == Display.console:
            return ConsoleDisplay()
        else:
            return GuiDisplay()

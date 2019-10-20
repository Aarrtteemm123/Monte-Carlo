from tkinter import *
from App import Application

root = Tk()
root.title("Monty Hall")
root.geometry("600x350+450+100")
root.wm_maxsize(width=600,height=350)
root.wm_minsize(width=600,height=350)
app = Application(root)
app.app_run()

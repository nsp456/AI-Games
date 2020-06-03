import tkinter as tk

root = tk.Tk()
T = tk.Text(root, height=10, width=60)
T.pack()
T.insert(tk.END, "\nThis AI game will first analyse every possible path to \nvictory and then it's speed of achieving victory will \nkeep on increasing until it reaches a point where it\nkeeps winning in every trial. \nGame will begin as soon as you close this Window\n\nENJOY !!!")
tk.mainloop()

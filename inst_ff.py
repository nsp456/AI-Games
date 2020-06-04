import tkinter as tk

root = tk.Tk()
root.title("Instructions for Flying Face")
T = tk.Text(root, height=12, width=60)
T.pack()
T.insert(tk.END, "\nDo you enjoy playing Flappy Bird ?\nIf yes then you will surely enjoy this AI Game as well.\nIn this game, your nose will act as a bird and your \nobjective is to not hit any of the rectangular bars.\nGame will begin as soon as you close this Window\n\nNOTE - The score is a measure of time and not of number \nof bars crossed.\n\nENJOY !!!")
tk.mainloop()

import tkinter as tk

root = tk.Tk()
root.title("Instructions for AI Learns")
T = tk.Text(root, height=11, width=60)
T.pack()
T.insert(tk.END, "\nIn the game, Top left corner shows the trial number.\nAt first the player moves randomly and it gets feedback \ndepending whether it gets closer or moves further away \nfrom the goal, and based on that it makes decision to \nget more positive feedback. If the player goes out of \nboundary, he dies and next trial begins. \nGame will begin as soon as you close this Window\n\nENJOY !!!")
tk.mainloop()

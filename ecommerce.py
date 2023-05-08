from tkinter import *


root = Tk()
root.title("ShopSpot - An E-Commerce Program")
root.geometry("1000x600")
root.configure(bg = "#659DBD")

browse = Frame(root)
cart = Frame(root)

heading = Label(root, text = "ShopSpot", font = ("Gabriola", 50), fg = "white", bg = "#659DBD")
heading.place(relx = 0.5, rely = 0.075, anchor=CENTER)

def exit():
    root.destroy()

browse_button = Button(root, text = "Browse Items", font = "Helvetica, 15", bg = "white", fg = "#659DBD")
cart_button = Button(root, text = "Go To Cart", font = "Helvetica, 15", bg = "white", fg = "#659DBD")
exit_button = Button(root, text = "Exit", font = "Helvetica, 13", bg = "#8D8741", fg = "white", command = exit, padx = 10)

browse_button.place(relx = 0.33, rely = 0.175, anchor=CENTER)
cart_button.place(relx = 0.67, rely = 0.175, anchor=CENTER)
exit_button.place(relx = 0.975, rely = 0.05, anchor=CENTER)


root.mainloop()
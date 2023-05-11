from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
from PIL import Image

root = Tk()
root.title("ShopSpot - An E-Commerce Program")
root.geometry("1360x1000")
root.configure(bg = "#659DBD")
root.attributes('-fullscreen', True)

browse = Frame(root, height = 500, width = 1400, bg = "#659DBD")
cart = Frame(root, height = 500, width = 1400, bg = "#659DBD")
browse.place(relx = 0.5, rely = 0.58, anchor=CENTER)
#cart.place(relx = 0.5, rely = 0.58, anchor=CENTER)
product = Frame(root, height = 1500, width = 1500, bg = "#659DBD")
product.place(relx =0.5, rely = 0.5, anchor = CENTER)

rootleft = Frame(root, height = 1000, width = 340, bg = "#DAAD86")
rootleft.place(relx = 0.1, rely = 0.5, anchor=CENTER)

heading = Label(root, text = "ShopSpot", font = ("Gabriola", 60), fg = "white", bg = "#8D8741", width = 1500)
heading.place(relx = 0.5, rely = 0.075, anchor=CENTER)


def exit():
    root.destroy()



def HideAllFrames():
    for widget in browse.winfo_children():
        widget.destroy()
    for widget in cart.winfo_children():
        widget.destroy()

Grocery_button=Button(rootleft,text="Grocery",font="times 20 bold",width=17,bd=6,bg="#659DBD",fg="white",activebackground="light blue",command=HideAllFrames)
Grocery_button.place(relx = 0.5, rely = 0.3, anchor = CENTER)

Electronics_button=Button(rootleft,text="Electronics",font="times 20 bold",width=17,bd=6,bg="#659DBD",fg="white",activebackground="light blue",command=HideAllFrames)
Electronics_button.place(relx = 0.5, rely = 0.37, anchor = CENTER)

Sports_Gym_button=Button(rootleft,text="Sports and Gym",font="times 20 bold",width=17,bd=6,bg="#659DBD",fg="white",activebackground="light blue",command=HideAllFrames)
Sports_Gym_button.place(relx = 0.5, rely = 0.44, anchor = CENTER)

Furniture_button=Button(rootleft,text="Furniture",font="times 20 bold",width=17,bd=6,bg="#659DBD",fg="white",activebackground="light blue",command=HideAllFrames)
Furniture_button.place(relx = 0.5, rely = 0.51, anchor = CENTER)

Appliances_button=Button(rootleft,text="Appliances",font="times 20 bold",width=17,bd=6,bg="#659DBD",fg="white",activebackground="light blue",command=HideAllFrames)
Appliances_button.place(relx = 0.5, rely = 0.58, anchor = CENTER)

Exit_button=Button(rootleft,text="EXIT",font="times 20 bold",width=17,bd=6,bg="#BC986A",fg="white",activebackground="light blue",command=exit)
Exit_button.place(relx = 0.5, rely = 0.8, anchor = CENTER)

#Images 
grocery_image = ImageTk.PhotoImage(Image.open("Images/grocery.png"))
grocery_label = Label(product, image=grocery_image, height= 320, width = 320)

appliances_image = ImageTk.PhotoImage(Image.open("Images/appliances.png"))
appliances_label = Label(product, image=appliances_image, height= 320, width = 320)

furniture_image = ImageTk.PhotoImage(Image.open("Images/furniture.png"))
furniture_label = Label(product, image=furniture_image, height= 325, width = 325)

gym_image = ImageTk.PhotoImage(Image.open("Images/gym.jpg"))
gym_label = Label(product, image=gym_image, height= 320, width = 320)

electronics_image = ImageTk.PhotoImage(Image.open("Images/electronics.png"))
electronics_label = Label(product, image=electronics_image, height= 320, width = 320)

#appliances_label.pack()
#gym_label.pack()
#electronics_label.pack()
#furniture_label.pack()
#grocery_label.pack()
root.mainloop()
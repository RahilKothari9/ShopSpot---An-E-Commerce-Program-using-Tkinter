from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk
from PIL import Image

root = Tk()
root.title("ShopSpot - An E-Commerce Program")
root.geometry("1360x1000")
root.configure(bg = "#659DBD")
root.attributes('-fullscreen', True)


product = Frame(root, height = 1500, width = 1500, bg = "#659DBD")
product.place(relx =0.5, rely = 0.5, anchor = CENTER)

rootleft = Frame(root, height = 1000, width = 340, bg = "#DAAD86")
rootleft.place(relx = 0.1, rely = 0.5, anchor=CENTER)

heading = Label(root, text = "ShopSpot", font = ("Gabriola", 60), fg = "white", bg = "#8D8741", width = 1500)
heading.place(relx = 0.5, rely = 0.075, anchor=CENTER)

#items

grocery_items = {"Flour": ["Rs.40/kg", 40], "Rice": ["Rs.50/kg", 50], "Bread" : ["Rs.35 per packet", 35], 
                 "Butter" : ["Rs. 50 per packet", 50], "Milk" : ["Rs.100/litre", 100]}

cart = {}
def exit():
    root.destroy()



def HideAllFrames():
    for widget in product.winfo_children():
        widget.destroy()
    

Exit_button=Button(rootleft,text="EXIT",font="times 20 bold",width=17,bd=6,bg="#ED2939",fg="white",activebackground="light blue",command=exit)
Exit_button.place(relx = 0.5, rely = 0.82, anchor = CENTER)

#Images 
grocery_image = ImageTk.PhotoImage(Image.open("Images/grocery.png"))

appliances_image = ImageTk.PhotoImage(Image.open("Images/appliances.png"))
appliances_label = Label(product, image=appliances_image, height= 320, width = 320)

furniture_image = ImageTk.PhotoImage(Image.open("Images/furniture.png"))
furniture_label = Label(product, image=furniture_image, height= 325, width = 325)

gym_image = ImageTk.PhotoImage(Image.open("Images/gym.jpg"))
gym_label = Label(product, image=gym_image, height= 320, width = 320)

electronics_image = ImageTk.PhotoImage(Image.open("Images/electronics.png"))
electronics_label = Label(product, image=electronics_image, height= 320, width = 320)

h = 0
def cartFunc():
    HideAllFrames()
    style = ttk.Style()
    
    style.theme_use('clam')
    style.configure("Treeview.Heading", font=("Times New Roman", 20))
    style.configure("Treeview",
                    rowheight = 35,
                    font = ("Times New Roman", 20)
                    )
    global h
    h = len(cart) + 2
    tree = ttk.Treeview(product, column=("Name", "Price", "Quantity", "Total"), show='headings', height=h)
    tree.configure()
    tree.column("# 1", anchor=CENTER)
    tree.heading("# 1", text="Name")
    tree.column("# 2", anchor=CENTER)
    tree.heading("# 2", text="Price")
    tree.column("# 3", anchor=CENTER)
    tree.heading("# 3", text="Quantity")
    tree.column("# 4", anchor=CENTER)
    tree.heading("# 4", text="Total")

    TotPrice = 0
    for item in cart:
        tree.insert('', 'end', text="1", values=cart[item])
        TotPrice += cart[item][3]
    
    tree.insert('', 'end', text = "1", values=[" ", " ", " ", " "])
    tree.insert('', 'end', text = "1", values=["Total Cost ", " ", " ", TotPrice])
    tree.place(relx=0.48, rely=0.4, anchor=CENTER)

    def remove():
        x = tree.selection()
        y = tree.item(x)
        cart.pop(y["values"][0])
        tree.delete(x)
        global h
        h -= 1
        tree.configure(height = h)

    def checkout():
        conf = messagebox.askyesno("Confirm", f"Are you sure you want to purchase the items in your cart and exit?")
        if(conf):
            root.destroy()

    remove_btn = Button(product,text="Remove",font="Helvetica 20",width=17,bg="#8D8741",fg="white",activebackground="light blue",command=remove,bd=4)
    remove_btn.place(relx= 0.88, rely = 0.45, anchor=CENTER)

    checkout_btn = Button(product,text="Checkout",font="Helvetica 20",width=17,bg="#8D8741",fg="white",activebackground="light blue",command=checkout,bd=4)
    checkout_btn.place(relx= 0.88, rely = 0.65, anchor=CENTER)

def GroceryFunc():
    HideAllFrames()
    image_label = Label(product, image=grocery_image, height= 320, width = 320)
    subheading = Label(product, text = "Grocery", font = ("Times New Roman", 30), bg="#FBEEC1")
    subheading.place(relx = 0.31, rely= 0.534, anchor=CENTER, width= 324)
    image_label.place(relx = 0.31, rely=0.41, anchor=CENTER)
   
    e_text = Label(product, text="Quantity:", width = 20, height = 1, font = ("Times New Roman", 25), bg="#659DBD")
    e_text.place(relx = 0.6, rely = 0.5, anchor = CENTER)
    e= Entry(product, width = 23, font=('Times New Roman', 20), justify=CENTER)
    e.place(relx = 0.79, rely = 0.5, anchor=CENTER)
    
    def updatePrice(event):
        Price.configure(text=(grocery_items[item.get()])[0])

    t_text = Label(product, text="Item:", width = 20, height = 1, font = ("Times New Roman", 25), bg="#659DBD")
    t_text.place(relx = 0.6, rely = 0.35, anchor = CENTER)
    item_names =  list(grocery_items.keys())
    item = StringVar()
    item.set(item_names[0])

    p_text = Label(product, text="Price:", width = 20, height = 1, font = ("Times New Roman", 25), bg="#659DBD")
    p_text.place(relx = 0.6, rely = 0.40, anchor = CENTER)
    Price = Label(product, text=(grocery_items[item.get()])[0], width = 21, height = 1, font = ("Times New Roman", 20))
    Price.place(relx = 0.789, rely = 0.4, anchor=CENTER)

    drop = OptionMenu(product, item, *item_names, command=updatePrice)
    drop.configure(width = 20, height = 1, font = ("Times New Roman", 20))
    drop.place(relx = 0.68, rely = 0.335)

    def submit():
        x = e.get()
        y = item.get()
        z = (grocery_items[y])[1] * int(x)
        conf = messagebox.askyesno("Confirm", f"Are you sure you want to purchase {x} items of {y} at total cost of Rs.{z}?")
        if(conf):
            if y in cart.keys():
                cart[y][2] += int(x)
                cart[y][3] = cart[y][2] * cart[y][1]
            else:
                cart[y] = [item.get(), grocery_items[y][1], int(x), z]
            messagebox.showinfo("Success", "Added to Cart")

    sub_btn = Button(product,text="Add To Cart",font="Helvetica 25",width=20,bg="#8D8741",fg="white",activebackground="light blue",command=submit,bd=4)
    sub_btn.place(relx= 0.75, rely = 0.65, anchor=CENTER)

def ElectronicsFunc():
    HideAllFrames()
    
    


#appliances_label.pack()
#gym_label.pack()
#electronics_label.pack()
#furniture_label.pack()
#grocery_label.pack()


Grocery_button=Button(rootleft,text="Grocery",font="times 20 bold",width=17,bd=6,bg="#659DBD",fg="white",activebackground="light blue",command=GroceryFunc)
Grocery_button.place(relx = 0.5, rely = 0.3, anchor = CENTER)

Electronics_button=Button(rootleft,text="Electronics",font="times 20 bold",width=17,bd=6,bg="#659DBD",fg="white",activebackground="light blue",command=ElectronicsFunc)
Electronics_button.place(relx = 0.5, rely = 0.37, anchor = CENTER)

Sports_Gym_button=Button(rootleft,text="Sports and Gym",font="times 20 bold",width=17,bd=6,bg="#659DBD",fg="white",activebackground="light blue",command=cartFunc)
Sports_Gym_button.place(relx = 0.5, rely = 0.44, anchor = CENTER)

Furniture_button=Button(rootleft,text="Furniture",font="times 20 bold",width=17,bd=6,bg="#659DBD",fg="white",activebackground="light blue",command=HideAllFrames)
Furniture_button.place(relx = 0.5, rely = 0.51, anchor = CENTER)

Appliances_button=Button(rootleft,text="Appliances",font="times 20 bold",width=17,bd=6,bg="#659DBD",fg="white",activebackground="light blue",command=HideAllFrames)
Appliances_button.place(relx = 0.5, rely = 0.58, anchor = CENTER)

cart_button=Button(rootleft,text="CART",font="times 20 bold",width=17,bd=6,bg="#8D8741",fg="white",activebackground="light blue",command=cartFunc)
cart_button.place(relx = 0.5, rely = 0.75, anchor = CENTER)

root.mainloop()
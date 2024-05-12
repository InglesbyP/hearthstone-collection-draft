import tkinter as tk
from PIL import Image, ImageTk


def create(images):
    root = tk.Tk()
    root.geometry('900x400')
    canvas = tk.Canvas(root,width=999,height=999)
    canvas.pack()
    # pilImage = Image.open("ball.gif")
    image = ImageTk.PhotoImage(images[0])
    imagesprite = canvas.create_image(200,200,image=image)
    
    image2 = ImageTk.PhotoImage(images[1])
    imagesprite2 = canvas.create_image(450,200,image=image2)
    
    image3 = ImageTk.PhotoImage(images[2])
    imagesprite3 = canvas.create_image(700,200,image=image3)
    
    root.mainloop()
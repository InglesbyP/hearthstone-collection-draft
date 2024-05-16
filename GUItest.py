import tkinter as tk
from PIL import Image, ImageTk

# clicked = 0

# root = tk.Tk()
# root.geometry('900x400')

# def get_clicked():
#     global clicked
#     return clicked

# def on_click(event):
#     global clicked
#     if event.widget.cget('image') == 'pyimage1':
#         clicked = 0
#     if event.widget.cget('image') == 'pyimage2':
#         clicked = 1
#     if event.widget.cget('image') == 'pyimage3':
#         clicked = 2
#     # root.destroy()

# def create(images):
#     global clicked
#     root = tk.Tk()
#     root.geometry('900x400')
#     clicked = 0
#     print("IN CREATE NOW")
#     print(images)
#     canvas = tk.Canvas(root,width=999,height=999)
#     canvas.pack()
#     image = ImageTk.PhotoImage(images[0])
#     button1 = tk.Button(canvas, image=image)
#     button1.bind('<Button-1>', on_click())
#     test = canvas.create_window(200, 200, window=button1)
    
#     image2 = ImageTk.PhotoImage(images[1])
#     button2 = tk.Button(canvas, image=image2)
#     button2.bind('<Button-1>', on_click())
#     test2 = canvas.create_window(450, 200, window=button2)
    
#     image3 = ImageTk.PhotoImage(images[2])
#     button3 = tk.Button(canvas, image=image3)
#     button3.bind('<Button-1>', on_click())
#     test3 = canvas.create_window(700, 200, window=button3)

#     root.mainloop()


class MyApplication:
    def __init__(self, root, images=None):
        self.root = root
        self.root.geometry('900x400')
        self.clicked = 0
        self.root.title("Hearthstone Collection Arena")
        
        self.images = images 
        # print("IN CREATE NOW")
        # print(images)

        canvas = tk.Canvas(root,width=999,height=999)
        canvas.pack()
        self.image = ImageTk.PhotoImage(images[0])
        button1 = tk.Button(canvas, image=self.image)

        button1.bind('<Button-1>', self.on_click(event=1))
        test = canvas.create_window(200, 200, window=button1)
        
        self.image2 = ImageTk.PhotoImage(images[1])
        button2 = tk.Button(canvas, image=self.image2)
        button2.bind('<Button-1>', self.on_click(event=2))
        test2 = canvas.create_window(450, 200, window=button2)
        
        self.image3 = ImageTk.PhotoImage(images[2])
        button3 = tk.Button(canvas, image=self.image3)
        button3.bind('<Button-1>', self.on_click(event=3))
        test3 = canvas.create_window(700, 200, window=button3)  
        

    def on_click(self, event):
        print("CLICKED NOW")
        # if event.widget.cget('image') == 'pyimage1':
        #     self.clicked = 0
        # if event.widget.cget('image') == 'pyimage2':
        #     self.clicked = 1
        # if event.widget.cget('image') == 'pyimage3':
        #     self.clicked = 2
        if event == 1:
            self.clicked = 0
        if event == 2:
            self.clicked = 1
        if event == 3:
            self.clicked = 2
        # self.destroy()
    
    def get_clicked(self):
        return self.clicked()

    def run(self):
        self.root.mainloop()
    
    def destroy(self):
        self.root.destroy()
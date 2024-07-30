from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Image viewer")
root.iconbitmap("spidy.ico")
root.configure(bg="black")

img_1 = ImageTk.PhotoImage(Image.open("spidy1.jpeg"))
img_2 = ImageTk.PhotoImage(Image.open("spidy2.jpeg"))
img_3 = ImageTk.PhotoImage(Image.open("spidy3.jpeg"))
img_4 = ImageTk.PhotoImage(Image.open("spidy4.jpg"))
img_5 = ImageTk.PhotoImage(Image.open("spidy5.jpg"))

img_list = [img_1,img_2,img_3,img_4,img_5]

my_label = Label(image=img_1)
my_label.grid(row=1, column=1, columnspan=3)

def Forward(fo_num):
    global my_label
    global button_back
    global button_exit
    global button_front

    my_label.grid_forget()
    my_label = Label(image=img_list[fo_num-1])
    my_label.grid(row=1, column=1, columnspan=3)
    button_back = Button(root, text="previous",command=lambda :back(fo_num-1))
    button_exit = Button(root, text="Exit", command=root.quit)
    button_front = Button(root, text="Next", command=lambda: Forward(fo_num+1))



    if fo_num == 5:
        button_front = Button(root, text="Next",state=DISABLED)


    button_back.grid(row=5, column=0)
    button_exit.grid(row=5, column=2)
    button_front.grid(row = 5, column = 4)

def back(fo_num):
    global my_label
    global button_back
    global button_exit
    global button_front

    my_label.grid_forget()
    my_label = Label(image=img_list[fo_num - 1])
    my_label.grid(row=1, column=1, columnspan=3)
    button_back = Button(root, text="previous", command=lambda: back(fo_num - 1))
    button_exit = Button(root, text="Exit", command=root.quit)
    button_front = Button(root, text="Next", command=lambda: Forward(fo_num + 1))

    if fo_num == 0:
        button_back = Button(root, text="previous", state=DISABLED)

    button_back.grid(row=5, column=0)
    button_exit.grid(row=5, column=2)
    button_front.grid(row=5, column=4)


button_back = Button(root, text = "previous",command=back,state=DISABLED)
button_exit = Button(root, text="Exit", command=root.quit)
button_front = Button(root, text="Next",command=lambda : Forward(2))


button_back.grid(row = 5, column = 0)
button_exit.grid(row=5, column=2)
button_front.grid(row = 5, column = 4)

root.mainloop()

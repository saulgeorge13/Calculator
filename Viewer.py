from os import stat
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('welcome lads')

# Add icon, needs to be ico file
#root.iconbitmap('C:\Users\sauls\Desktop\GUI\')

maxImages = 5
img1 = ImageTk.PhotoImage(Image.open("Images/image1.jpg"))
img2 = ImageTk.PhotoImage(Image.open("Images/image2.jpg"))
img3 = ImageTk.PhotoImage(Image.open("Images/image3.jpg"))
img4 = ImageTk.PhotoImage(Image.open("Images/image4.jpg"))
img5 = ImageTk.PhotoImage(Image.open("Images/image5.jpg"))

imageList = [img1, img2, img3, img4, img5]

myLabel = Label(image=img1)
myLabel.grid(row=0, column=0, columnspan=3)

def forward_button(imageNumber):
    # Define global variables to update
    global myLabel
    global buttonForward
    global buttonBack
    # Clear label
    myLabel.grid_forget()
    # Get next image onto label and update buttons
    myLabel = Label(image=imageList[imageNumber-1])
    buttonBack = Button(root, text="<<", command=lambda: back_button(imageNumber-1))
    if imageNumber == maxImages:
        buttonForward = Button(root, text=">>", state=DISABLED)
    else:
        buttonForward = Button(root, text=">>", command=lambda: forward_button(imageNumber+1))
    # Place updated label and buttons
    myLabel.grid(row=0, column=0, columnspan=3)
    buttonForward.grid(row=1, column=2)
    buttonBack.grid(row=1, column=0)

def back_button(imageNumber):
     # Define global variables to update
    global myLabel
    global buttonForward
    global buttonBack
    # Clear label
    myLabel.grid_forget()
    # Get next image onto label and update buttons
    myLabel = Label(image=imageList[imageNumber-1])
    buttonForward = Button(root, text=">>", command=lambda: forward_button(imageNumber+1))
    if imageNumber == 1:
        buttonBack = Button(root, text="<<", state=DISABLED)
    else:
        buttonBack = Button(root, text="<<", command=lambda: back_button(imageNumber-1))
    # Place updated label and buttons
    myLabel.grid(row=0, column=0, columnspan=3)
    buttonForward.grid(row=1, column=2)
    buttonBack.grid(row=1, column=0)

buttonBack = Button(root, text="<<", command=back_button, state=DISABLED)
buttonQuit = Button(root, text="Exit Program", command=root.quit)
buttonForward = Button(root, text=">>", command=lambda: forward_button(2))
buttonBack.grid(row=1, column=0)
buttonQuit.grid(row=1, column=1)
buttonForward.grid(row=1, column=2)


root.mainloop()



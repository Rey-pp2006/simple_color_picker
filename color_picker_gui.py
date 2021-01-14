"""
Create a simple color picker
@author: Reyhaneh :)

"""

#import modules
from tkinter import *
from tkinter import colorchooser
from PIL import Image, ImageTk

#make a gui window
root = Tk()

#set a title for the window
root.title("Color picker")

# set the wimdow's size 
root.geometry("400x300")
root.minsize(200, 300)
root.maxsize(200, 300)

# set a background color
root.config(bg="#ffffff")

#add an image 
img = Image.open("Img/pic.jpg")
img = img.resize((200,100))
imsge  = ImageTk.PhotoImage(img)

image_lab=Label(root,image=imsge)
image_lab.place(x=0,y=200)

#this function chooses a color and print the hex code and rgb 
def color_picker():
    #pick a color
    color=colorchooser.askcolor()
    
    color_lab=Label(root, text=" # You choosed a color!  ",fg="#000000",bg=color[1] , bd=5,font="Aharoni 13 bold")
    color_lab.grid(row=1, column=0)
    
    color_lab_hex=Label(root, text=f"hex code : {color[1] }",fg=color[1],bg="#ffffff" , bd=5,font="Aharoni 10 bold")
    color_lab_hex.grid(row=2, column=0)
    
    color_lab_r=Label(root, text=f" Red: {int(color[0][0])}",fg="red",bg="#ffffff" , bd=5,font="Aharoni 10 bold")
    color_lab_r.grid(row=3, column=0)
    
    color_lab_g=Label(root, text=f" Green: {int(color[0][1])}",fg="green",bg="#ffffff" , bd=5,font="Aharoni 10 bold")
    color_lab_g.grid(row=4, column=0)
    
    color_lab_b=Label(root, text=f" Blue: {int(color[0][2])}",fg="blue",bg="#ffffff" , bd=5,font="Aharoni 10 bold")
    color_lab_b.grid(row=5, column=0 ,pady=(0,10))

#pick color button
choose_button=Button(root,text = "pick a color " ,command=color_picker,bg="#99003d",fg="#ffffff" , bd=5,font="Aharoni 12 bold")
choose_button.grid(row=0, column=0 , ipadx = 45 ,pady=(0,17))

#start the program
root.mainloop()

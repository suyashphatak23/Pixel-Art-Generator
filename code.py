'''
Pixel Art Generator
@author : Suyash Shivaji Phatak
Date: 12/5/2020
'''

# Importing Libraries
from tkinter import *
import tkinter as tk
from tkinter import messagebox as ms
from tkinter import filedialog
from PIL import ImageTk, Image 
import time, os

# Creating Window
root = tk.Tk()

# Creating Window of Desired Size
root.geometry('500x500')

# Locking the window size
root.resizable(width=False, height=False)

# Creating Title
root.title('Pixel Art Generator')

# Creating title icon
root.iconbitmap('img/logo.ico')

# Function for opening a image
def open_img():
    global my_image

    # Error Handling
    try:
        # Uploading File
        root.filename = filedialog.askopenfilename(initialdir='img', title='Select A File', filetypes=(('All Files', '*.*'), ('JPG files','*.jpg'),('JPEG files','*.jpeg'),('GIF files','*.gif'),('PNG files','*.png')))

        # Original Image
        original_image = Image.open(root.filename)

        # Copying image to another variable
        my_image = original_image

        # Process to convert into pixel art
        process = my_image.resize((128,128), Image.BILINEAR)
        result_image = process.resize(my_image.size, Image.NEAREST)

        # Saving as new file and changing file name if name exists
        if os.path.exists('result.png'):
            result_image.save('result_{}.png'.format(int(time.time())))
        else:
            result_image.save('result.png')

        # Thanking Message
        if result_image.save:
            response = ms.askyesno('Converted Successfully !!!', 'Thank You For Using Our Sevice.\nPlease See Your Current File or Code Directory.\nDo You Want To Exit Converter ?')

            # Creating Response answer
            if response == 1:
                root.destroy()
            else:
                pass
    except:
        ms.showerror('Error', 'Please Select a Image !!!')

''' Background Image Start'''
# Sizing Image
canvas = Canvas(root, height= 500, width=500)

# Opening Image
image = ImageTk.PhotoImage(Image.open('img/pixelbg.jpg'))

#Positioning Image
canvas.create_image(0,0, anchor=NW, image=image)
canvas.pack(fill='both')
''' Background Image End'''

# Creating Frame
frame = LabelFrame(root, padx=10, pady=20, bg='white', bd='5', relief='groove')
frame.place(relx = 0.5, rely = 0.5, anchor = CENTER)

# Giving Info
my_label = Label(frame, text='Convert Image To Pixel Art', font=('Arial',12, 'bold'),bg='white', fg='red').pack()

# Label for seperating Buttons
label = Label(frame, bg='white').pack()

# Creating a uplod button
file = Button(frame, text='Upload a Image', command = open_img, width="15", bd = '3', font = ('Times', 12, 'bold'), bg='indigo', fg='white',relief='groove', justify = 'center', pady='3').pack()

root.mainloop()

import tkinter as tk
#to make GUI using python
from PIL import Image, ImageTk
#to use images in the GUI
from tkinter import font
#to use fonts in the GUI
from tkinter import messagebox
#for showing alerts 
root = tk.Tk()
root.title("My First GUI")
#to set the title of the window
root.geometry("500x600")
#to set the size of the window
'''root.iconbitmap("icon.ico")
#to set the icon of the window'''
root.minsize(300, 300)
root.maxsize(600, 600)
#to set the minimum and maximum size of the window
root.configure(bg="#0f4c2e")
img = Image.open("ChatGPT Image Jun 4, 2025 at 10_51_20 PM.png")
#to open the image file
resized_img = img.resize((90, 90))
#to resize the image to fit in the window
img = ImageTk.PhotoImage(resized_img)
img_label = tk.Label(root, image=img)
img_label.pack(pady=(10,10))
text_frame = tk.Frame(root, bg="#0f4c2e")
text_frame.pack(pady=(10, 0), anchor='e', fill='x')
# THE (all caps, bold)
label_the = tk.Label(root, text="The", font=("Brush Script MT", 17),
                     fg="#d6f9d8", bg="#0f4c2e")
label_the.pack()

# Granny’s (script-like)
label_granny = tk.Label(root, text="Granny’s", font=("Brush Script MT", 17),
                        fg="#d6f9d8", bg="#0f4c2e")
label_granny.pack()

# TRUNK (bold, uppercase)
label_trunk = tk.Label(root, text="Trunk", font=("Brush Script MT", 17),
                       fg="#d6f9d8", bg="#0f4c2e")
label_trunk.pack()

email_label = tk.Label(root, text="Email:", font=("Arial", 12),
                       fg="#d6f9d8", bg="#0f4c2e")
email_label.pack(pady=(25, 5))

email_input = tk.Entry(root, font=("Arial", 12), width=40)
email_input.pack(ipady=6, pady=(0, 20), padx=10)
#to create an input field for email 
password_label = tk.Label(root, text="Password:", font=("Arial", 12),
                       fg="#d6f9d8", bg="#0f4c2e")
password_label.pack(pady=(25, 5))

password_label = tk.Entry(root, font=("Arial", 12), width=40)
password_label.pack(ipady=6, pady=(0, 20), padx=10)
login_button = tk.Button(root, text="Login", font=("Arial", 12),fg="#0f4c2e", bg="#d6f9d8")
login_button.pack(pady=(15, 10), padx=10, fill='x')
#to create a button for login
login_button.bind("<Button-1>", lambda e: messagebox.showinfo("Login", "Login button clicked!"))
#to show an alert when the login button is clicked
root.mainloop()
#to run the main loop of the window
#this will keep the window open until closed by the user
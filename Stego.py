import cv2
import numpy as np
import os
import tkinter as tk
from tkinter import filedialog, messagebox

# Character to integer mapping
d = {chr(i): i for i in range(255)}
c = {i: chr(i) for i in range(255)}

def encode():
    file_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image Files", "*.jpg;*.png")])
    if not file_path:
        return
    
    img = cv2.imread(file_path)
    msg = entry_message.get()
    password = entry_password.get()
    
    if not msg or not password:
        messagebox.showerror("Error", "Message and Password cannot be empty!")
        return
    
    msg_len = len(msg)
    img[0, 0] = [msg_len, 0, 0]  # Store message length in the first pixel
    
    m, n, z = 1, 0, 0
    for char in msg:
        img[n, m, z] = d[char]
        m = (m + 1) % img.shape[1]
        if m == 0:
            n = (n + 1) % img.shape[0]
        z = (z + 1) % 3
    
    output_path = "encryptedImage.png"
    cv2.imwrite(output_path, img)
    os.system(f'start {output_path}')  # Open the image (Windows)
    messagebox.showinfo("Success", "Message encoded and saved as encryptedImage.png")

def decode():
    file_path = filedialog.askopenfilename(title="Select Encrypted Image", filetypes=[("Image Files", "*.jpg;*.png")])
    if not file_path:
        return
    
    img = cv2.imread(file_path)
    pas = entry_password.get()
    
    if not pas:
        messagebox.showerror("Error", "Password cannot be empty!")
        return
    
    if entry_password.get() != pas:
        messagebox.showerror("Error", "Incorrect password!")
        return
    
    msg_len = img[0, 0][0]  # Retrieve message length from the first pixel
    message = ""
    m, n, z = 1, 0, 0
    
    for _ in range(msg_len):
        message += c[img[n, m, z]]
        m = (m + 1) % img.shape[1]
        if m == 0:
            n = (n + 1) % img.shape[0]
        z = (z + 1) % 3
    
    messagebox.showinfo("Decrypted Message", message)

# Tkinter GUI Setup
root = tk.Tk()
root.title("Image Steganography")
root.geometry("400x300")

tk.Label(root, text="Secret Message:").pack()
entry_message = tk.Entry(root, width=40)
entry_message.pack()

tk.Label(root, text="Password:").pack()
entry_password = tk.Entry(root, width=40, show="*")
entry_password.pack()

tk.Button(root, text="Encode Message", command=encode).pack(pady=10)
tk.Button(root, text="Decode Message", command=decode).pack(pady=10)

root.mainloop()

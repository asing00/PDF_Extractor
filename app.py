import tkinter as tk
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk

import PyPDF2

root = tk.Tk()

canvas = tk.Canvas(root, width=500, height=300)
canvas.grid(columnspan=3, rowspan=3)

logo = Image.open("logo.png")
logo = logo.resize((200,150))
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)


instructions = tk.Label(root, text="Select a PDF file on PC to extract it's text", font="Arial")
instructions.grid(columnspan=3, column=0, row=1)

def open_file():
    browse_text.set("Loading...")
    file = askopenfile(parent=root, mode="rb", title="Select a file", filetype=[("Pdf file", "*.pdf")])
    if file:
        read_pdf = PyPDF2.PdfFileReader(file)
        page = read_pdf.getPage(0)
        content_page = page.extract_text()
        
        text_box = tk.Text(root, height=9, width=50, padx=15, pady=15)
        text_box.insert(1.0, content_page)
        text_box.tag_configure("center", justify="center")
        text_box.tag_add("center", 1.0, "end")
        text_box.grid(column=1, row=3)

        browse_text.set("Browse")


browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, command=lambda:open_file(), font="Arial", bg="red", fg="white", height=1, width=10)
browse_text.set("Browse")
browse_btn.grid(column=1, row=2)

canvas = tk.Canvas(root, width=500, height=250)
canvas.grid(columnspan=3)


root.mainloop()


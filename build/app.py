# Author: Sufiyaan Usmani (https://github.com/sufiyaanusmani)
# Email: usmanisufiyaan@gmail.com
# Repository Link: git@github.com:sufiyaanusmani/PNG-To-ICO-Converter.git


from pathlib import Path
import os
import sys
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import tkinter.filedialog
import tkinter.messagebox
from PIL import Image
# import win32gui
# import win32con


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")
output_path = ""
path = getattr(sys, '_MEIPASS', os.getcwd())
os.chdir(path)


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def select_path1():
    global output_path

    output_path = tkinter.filedialog.askopenfile(
        mode='r', filetypes=[('Images', '*.png')])
    start = str(output_path).index("'") + 1
    end1 = str(output_path).index(".png") + 4
    output_path = str(output_path)[start:end1]
    entry_1.delete(0, tkinter.END)
    entry_1.insert(0, output_path)


def select_path2():
    global output_path

    output_path = tkinter.filedialog.askdirectory()
    entry_2.delete(0, tkinter.END)
    entry_2.insert(0, output_path)


def convert():
    source = entry_1.get().strip()
    destination = entry_2.get().strip()
    destination = destination + "/" + "img.ico"

    if not source:
        tkinter.messagebox.showerror(
            title="Source not entered!", message="Please select image")
        return
    if not destination:
        tkinter.messagebox.showerror(
            title="Destination not entered!", message="Please select destination")
        return
    if ".png" not in source:
        tkinter.messagebox.showerror(
            title="Wrong File", message="Please select valid png file")
        return

    try:
        img = Image.open(source)
        img.save(destination, sizes=[(48, 48)])
        tkinter.messagebox.showinfo(
            title="Success", message="Image converted successfully")
    except Exception as e:
        print(e)


# hide = win32gui.GetForegroundWindow()
# win32gui.ShowWindow(hide, win32con.SW_HIDE)
window = Tk()
window.title("PNG To ICO Converter")
window.geometry("300x250")
window.eval('tk::PlaceWindow . center')
window.configure(bg="#FFFFFF")


canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=250,
    width=300,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
canvas.create_text(
    11.0,
    24.0,
    anchor="nw",
    text="Browse For File",
    fill="#000000",
    font=("Inter Light", 13 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    133.5,
    62.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#ECE8E8",
    highlightthickness=0
)
entry_1.place(
    x=20.0,
    y=52.0,
    width=227.0,
    height=18.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=select_path1,
    relief="flat"
)
button_1.place(
    x=263.0,
    y=52.0,
    width=26.0,
    height=20.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=convert,
    relief="flat"
)
button_2.place(
    x=11.0,
    y=184.0,
    width=275.0,
    height=38.0
)

canvas.create_text(
    11.0,
    97.0,
    anchor="nw",
    text="Destination",
    fill="#000000",
    font=("Inter Light", 13 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    133.5,
    135.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#ECE8E8",
    highlightthickness=0
)
entry_2.place(
    x=20.0,
    y=125.0,
    width=227.0,
    height=18.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=select_path2,
    relief="flat"
)
button_3.place(
    x=263.0,
    y=125.0,
    width=26.0,
    height=20.0
)

canvas.create_text(
    29.0,
    232.0,
    anchor="nw",
    text="Sufiyaan Usmani (https://github.com/sufiyaanusmani)",
    fill="#000000",
    font=("Inter ExtraLight", 10 * -1)
)
window.resizable(False, False)
window.mainloop()

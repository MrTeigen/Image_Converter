import tkinter as tk
from tkinter import ttk
import tkinterDnD
from PIL import Image
import os

# You have to use the tkinterDnD.Tk object for super easy initialization,
# and to be able to use the main window as a dnd widget
root = tkinterDnD.Tk()  
root.title("Image Converter")
root.geometry("200x80")

# I use grid for easy resizing
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

# Placing the frames in the grid
drop_down_frame = ttk.Frame(root, width=400, height=200, relief="solid")
drop_down_frame.grid(column=0, row=0, sticky="nsew")

# Initializing the Variables
stringvar = tk.StringVar()
stringvar.set('Select Target File Type:')

option_var = tk.StringVar()
option_var.set("JPEG")

# I have not tested all of these, but the ones I have tested works
read_set = {"BLP",
            "BMP",
            "CUR",
            "DCX",
            "DDS",
            "DIB",
            "EMF",
            "EPS",
            "FITS",
            "FLC",
            "FLI",
            "FPX",
            "FTEX",
            "GBR",
            "GD",
            "GIF",
            "ICNS",
            "ICO",
            "IM",
            "IMT",
            "IPTC",
            "JPEG",
            "JP2",
            "JPG",
            "JPX"
            "MCIDAS",
            "MIC",
            "MPO",
            "MSP",
            "NAA",
            "PCD",
            "PCX",
            "PIXAR",
            "PNG",
            "PPM",
            "PSD",
            "SGI",
            "SPI",
            "SUN",
            "TGA",
            "TIFF",
            "WAL",
            "WEBP",
            "WMF",
            "XBM",
            "XPM"}

# This is the list of file types we can convert to
# We can also implement the following file types: BLP, MSP, PALM and XBM
options =  ["JPEG",
            "BMP",
            "DDS",
            "DIB",
            "EPS",
            "GIF",
            "ICNS",
            "ICO",
            "IM",
            "JPEG",
            "JPEG 2000",
            "PCX",
            "PDF",
            "PNG",
            "PPM",
            "SGI",
            "SPIDER",
            "TGA",
            "TIFF",
            "WebP"]


# When a file is dragged over the widget,
# this function changes the stringvar text to the file path
def show_item(event):
    stringvar.set(event.data)


# This function is called, when stuff is dropped into the widget
# It converts the image to the selected file type
# and saves it in the same folder as the original image
# If the file type is not supported, it returns an error message
def drop(event):
    stringvar.set("Working...")
    for i in root.tk.splitlist(event.data):
        j = i[1:-1] if i[0] == '{' else i
        if j.rsplit(".", 1)[-1].upper() in read_set:
            try:
                match option_var.get():
                    case "JPEG 2000":
                        image = Image.open(j).convert("RGB")
                        image.save(j.rsplit(".", 1)[0] + ".jp2")
                    case "SPIDER":
                        image = Image.open(j).convert("RGBA")
                        image.save(j.rsplit(".", 1)[0] + ".spi", format="SPIDER")
                    case "ICO" | "PNG" | 'GIF':
                        image = Image.open(j).convert("RGBA")
                        image.save(j.rsplit(".", 1)[0] + "." + option_var.get().lower(), format=option_var.get())
                    case _:
                        image = Image.open(j).convert("RGB")
                        image.save(j.rsplit(".", 1)[0] + "." + option_var.get().lower())
            except Exception:
                stringvar.set("Error!")
                return
        else:
            stringvar.set("Invalid file type!")
            return
    stringvar.set("Done!")

# Placing the widgets in their respective frames
drop_down_label = ttk.Label(drop_down_frame, textvariable=stringvar)
drop_down_label.pack(padx=10, pady=(10, 0))

drop_down = ttk.OptionMenu(drop_down_frame, option_var, *options, )
drop_down.pack(padx=10, pady=10)

# Binding the widgets to the drop and show functions
drop_down_frame.register_drop_target("*")
drop_down_frame.bind("<<Drop>>", drop)
drop_down_frame.register_drag_source("*")
drop_down_frame.bind("<<DropEnter>>", show_item)

# Starting the mainloop
if __name__ == "__main__":
    root.mainloop()
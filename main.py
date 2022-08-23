import tkinter as tk
from tkinter import ttk
# from PIL import Image, ImageTk


def get_entry():
    selected = selected_conversion.get()
    value = float(entry.get())
    if selected.lower() == "mm":
        output_value.set(f"the conversion: {value*1000} mm")
    elif selected.lower() == "cm":
        output_value.set(f"the conversion: {value*100} cm")
    elif selected.lower() == "meter":
        output_value.set(f"the conversion: {value} m")
    elif selected.lower() == "km":
        output_value.set(f"the conversion: {value/1000} km")
    elif selected.lower() == "mile":
        output_value.set(f"the conversion: {value/1609} mile")
    elif selected.lower() == "feet":
        output_value.set(f"the conversion: {value*3.28} feet")
    elif selected.lower() == "inch":
        output_value.set(f"the conversion: {value*39.37} feet")
    


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Distance Converter")
    root.geometry("400x100")
    root.resizable(False, False)

    frame1 = ttk.Frame(root)
    frame1.pack()

    frame2 = ttk.Frame(root)
    frame2.pack()

    frame3 = ttk.Frame(root)
    frame3.pack()

    # frame 1
    entry = tk.StringVar(value="0.0")
    ttk.Label(frame1, text="Enter the Value:", padding=10).pack(side="left")
    input_entry = ttk.Entry(frame1, width=20, textvariable=entry)
    input_entry.pack(side="left")
    ttk.Label(frame1, text="m", padding=10).pack(side="left")

    # frame 2
    selected_conversion = tk.StringVar(value="mm")
    selection = ttk.Combobox(frame2, textvariable=selected_conversion)
    selection["values"] = ("mm", "cm", "meter", "km", "mile", "inch", "feet")
    selection["state"] = "readonly"
    selection.pack(side="left")
    button = ttk.Button(frame2, text="Print", command=get_entry)
    button.pack(side="left")
    ttk.Button(frame2, text="Quit", command=root.destroy).pack(side="left")

    # frame 3
    output_value = tk.StringVar(value="result shown here")
    output = ttk.Label(frame3, textvariable=output_value)
    output.pack()

    root.mainloop()

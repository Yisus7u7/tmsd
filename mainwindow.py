#!/data/data/com.termux/files/usr/bin/python3
# Made by Yisus7u7
print("""
        Mate Settings
        Made by @Yisus7u7
        """)
import tkinter as tk
#from tkinter import *
from tkinter import ttk
import exec_call as execute

root = tk.Tk()
root.title("mate-settings")
root.geometry("300x400")
root.resizable(False, False)
root.tk.call("wm", "iconphoto", root._w, tk.PhotoImage(file="./settings.png"))
# Import the tcl file
# Just simply import the sun-valley.tcl file
root.tk.call("source", "./theme/sun-valley.tcl")
# Then set the theme you want with the set_theme procedure
#widget.tk.call("set_theme", "light")
# or
root.tk.call("set_theme", "dark")

widget = tk.Frame(root, bd=25)
widget.pack(fill='both', expand=1)
look = ttk.Button(widget, 
        text="Appearance", 
        style="Accent.TButton",
        width=28,
        command=lambda: execute.style())
wms = ttk.Button(widget, 
        text="WM Settings", 
        style="Accent.TButton",
        width=28,
        command=lambda: execute.wm_settings())
wmtws = ttk.Button(widget,
        text="Tweaks Settings",
        style="Accent.TButton",
        width=28,
        command=lambda: execute.wm_tweaks_settings())
wmsp = ttk.Button(widget,
        text="Workspace Settings",
        style="Accent.TButton",
        width=28,
        command=lambda: execute.workspace_settings())
dfa = ttk.Button(widget,
		text="Default Applications",
		style="Accent.TButton",
		width=28,
		command=lambda: execute.df_apps_settings())
xsesion = ttk.Button(widget,
        text="Mate Session Settings",
        style="Accent.TButton",
        width=28,
        command=lambda: execute.mate_ss_settings())

mate_logo = tk.PhotoImage(file="./desktopenvironmentmate.png")

logo = ttk.Label(widget,
		image=mate_logo)

look.grid(row=0, column=0, pady=5)
wms.grid(row=1, column=0, pady=5)
wmtws.grid(row=2, column=0, pady=5)
wmsp.grid(row=3, column=0, pady=5)
dfa.grid(row=4, column=0, pady=5)
xsesion.grid(row=5, column=0, pady=5)
logo.grid(row=6, column=0)

root.mainloop()

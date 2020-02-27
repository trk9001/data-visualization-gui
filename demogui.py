#! /usr/bin/env python3

"""Script to drive a GUI for data visualization using tkinter."""

from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Sensor Data Visualization | NSU Satellite Team')
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

main_frame = ttk.Frame(root, width=1280, height=720, padding='5 5')
main_frame.grid(column=0, row=0, sticky='nwes')
main_frame.grid_propagate(0)  # Disable auto-sizing of master

main_frame.columnconfigure(0, weight=1)
main_frame.columnconfigure(2, pad=5)
main_frame.rowconfigure(0, pad=5)
main_frame.rowconfigure((1, 2), weight=1)
main_frame.rowconfigure(3, pad=5)

lbl = ttk.Label(main_frame, text='Real-time temperature data from sensors')
lbl.grid(column=0, row=0, columnspan=2, sticky='nwe')

lbox = Listbox(main_frame)
lbox.grid(column=0, row=1, rowspan=2, sticky='nwes')
sbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=lbox.yview)
sbar.grid(column=1, row=1, rowspan=2, sticky='ns')
lbox['yscrollcommand'] = sbar.set

btn = ttk.Button(main_frame, text='Test button')
btn.grid(column=2, row=2, sticky='se')

status = ttk.Label(main_frame, text='Selected: Nothing', anchor='w')
status.grid(column=0, row=3, sticky='we')

ttk.Sizegrip(main_frame).grid(column=2, row=3, sticky='se')

root.mainloop()

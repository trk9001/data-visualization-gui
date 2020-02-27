#! /usr/bin/env python3

"""Script to drive a GUI for data visualization using tkinter."""

import datetime as dt
import random
import threading
import time

from tkinter import *
from tkinter import ttk

MAX_DATA_ENTRIES = 100  # Max number of entries to show in the Listbox

root = Tk()
root.title('Sensor Data Visualization | NSU Satellite Team')
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

main_frame = ttk.Frame(root, width=700, height=500, padding='5 5')
main_frame.grid(column=0, row=0, sticky='nwes')
main_frame.grid_propagate(0)  # Disable auto-sizing of master

main_frame.columnconfigure(0, weight=1)
main_frame.columnconfigure(2, pad=5)
main_frame.rowconfigure(0, pad=5)
main_frame.rowconfigure((1, 2), weight=1)
main_frame.rowconfigure(3, pad=5)

lbl = ttk.Label(main_frame, text='Real-time temperature data from sensors')
lbl.grid(column=0, row=0, columnspan=2, sticky='nwe')

lbox = Listbox(main_frame, activestyle=NONE)
lbox.grid(column=0, row=1, rowspan=2, sticky='nwes')
sbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=lbox.yview)
sbar.grid(column=1, row=1, rowspan=2, sticky='ns')
lbox['yscrollcommand'] = sbar.set

status = ttk.Label(main_frame, text='Latest entry: None', anchor='w')
status.grid(column=0, row=3, sticky='we')

populate_listbox_stop_event = threading.Event()


def populate_listbox(interval_secs=1.0):
    """Dummy data feed (randomized)."""
    random.seed()
    while not populate_listbox_stop_event.is_set():
        temperature = float(random.randint(180, 280)) + random.random()
        temperature_entry = f'{temperature:.2f} K ({dt.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")})'
        lbox.insert(END, temperature_entry)
        lbox.see(END)
        if lbox.index(END) > MAX_DATA_ENTRIES:
            lbox.delete(0)
        status['text'] = f'Latest entry: {temperature_entry}'
        time.sleep(interval_secs)


threading.Thread(target=populate_listbox).start()


def trigger_populate_listbox_stop():
    """Callback to terminate the data-feed thread."""
    populate_listbox_stop_event.set()


btn = ttk.Button(main_frame, text='Stop Feed')
btn['command'] = trigger_populate_listbox_stop
btn.grid(column=2, row=2, sticky='se')

ttk.Sizegrip(main_frame).grid(column=2, row=3, sticky='se')

root.mainloop()

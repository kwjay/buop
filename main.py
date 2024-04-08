from tkinter import *
from tkinter import ttk

from BackupModule import BackupModule


bm = BackupModule()
root = Tk()
root.resizable(False, False)
root.geometry('300x150')
frame = ttk.Frame(root, padding=10)


device_open_button = ttk.Button(
    root,
    text='Open gallery directory',
    command=bm.select_device_dir
)
device_open_button.pack(expand=True)


backup_open_button = ttk.Button(
    root,
    text='Open backup directory',
    command=bm.select_backup_dir
)
backup_open_button.pack(expand=True)

root.mainloop()

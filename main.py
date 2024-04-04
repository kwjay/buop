from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo


class BackupModule:
    device_dir_path = ''
    backup_dir_path = ''

    def set_device_path(self, path):
        self.device_dir_path = path

    def set_backup_path(self, path):
        self.backup_dir_path = path

    def get_device_path(self):
        return self.device_dir_path

    def get_backup_path(self):
        return self.backup_dir_path


bm = BackupModule()
root = Tk()
root.resizable(False, False)
root.geometry('300x150')
frame = ttk.Frame(root, padding=10)


def select_device_dir():

    device_dir = fd.askdirectory(
        mustexist=True,
        title='Select directory')

    showinfo(
        title='Selected Directory',
        message=device_dir
    )

    bm.set_device_path(device_dir)


open_button = ttk.Button(
    root,
    text='Open dir',
    command=select_device_dir
)
open_button.pack(expand=True)


root.mainloop()

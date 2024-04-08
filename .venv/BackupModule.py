from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import os
import shutil

class BackupModule:
    device_dir = ''
    backup_dir = ''

    def select_device_dir(self):
        self.device_dir = fd.askdirectory(
            mustexist=True,
            title='Select device directory')

        showinfo(
            title='Selected Directory',
            message=self.device_dir
        )

    def select_backup_dir(self):
        self.backup_dir = fd.askdirectory(
            title='Select backup directory')

        showinfo(
            title='Selected Directory',
            message=self.backup_dir
        )
        self.start_backup()

    def start_backup(self):
        with os.scandir(self.device_dir) as directory:
            for file in directory:
                print(file)

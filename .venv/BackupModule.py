from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from datetime import datetime as dt
import os
import shutil

class BackupModule:
    device_dir = ''
    backup_dir = os.path.expanduser('~\\Documents\\backup')

    def select_device_dir(self):
        self.device_dir = fd.askdirectory(
            mustexist=True,
            title='Select device directory')

        showinfo(
            title='Selected Directory',
            message=self.device_dir
        )
        self.start_backup()


    def start_backup(self):
        print(self.backup_dir)
        if not os.path.exists(self.backup_dir):
            os.mkdir(self.backup_dir)
        with os.scandir(self.device_dir) as directory:
            for file in directory:
                file_stat = os.stat(file.path)
                file_date = dt.fromtimestamp(file_stat.st_mtime)
                year_dir = self.backup_dir + '\\' + str(file_date.year)
                if not os.path.exists(year_dir):
                    os.mkdir(year_dir)
                month_dir = year_dir + '\\' + file_date.strftime("%b")
                if not os.path.exists(month_dir):
                    os.mkdir(month_dir)

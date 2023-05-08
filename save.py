import shelve
from param import *

class Save:
    def __init__(self):
        self.file=shelve.open('data')

    def save(self):
        self.file['john_skin_on']=john_skin_on
        self.file['lang']=lang
        self.file['fullscreen']=fullscreen

    def add(self, name, value):
        self.file[name]=value

    def get(self, name):
        return self.file[name]

    def __del__(self):
        self.file.close()
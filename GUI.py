import tkinter
import Compress


class Gui:
    def __init__(self, mColor, bColor):
        self.__mColor = mColor
        self.__bColor = bColor
        self.__window = 0
        self.__en = 0

    def __makeItShorter(self):
        path = self.__en.get()
        cmprs = Compress.Compress(path)
        cmprs.compression()
        self.__window.destroy()

    def __makeItLonger(self):
        path = self.__en.get()
        dcmprs = Compress.Compress(path)
        dcmprs.decompress()
        self.__window.destroy()

    def mkGui(self):
        self.__window = tkinter.Tk()
        self.__en = tkinter.Entry(self.__window, width=58, bg=self.__bColor, fg=self.__mColor, borderwidth=10)
        compbutton = tkinter.Button(self.__window, width=50, bg='red', fg='black', text='compress', borderwidth=7, command=self.__makeItShorter)
        decompbutton = tkinter.Button(self.__window, width=50, bg='orange', fg='blue', text='decompress', borderwidth=7, command=self.__makeItLonger)
        self.__en.pack()
        compbutton.pack()
        decompbutton.pack()
        self.__window.mainloop()
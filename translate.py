import translators as tr
from tkinter import *
from tkinter import ttk

class Translator:
    def __init__(self):
        self.window = Tk()
        self.window.title('Translator')
        self.window.geometry('300x250')

        self.test = StringVar()
        self.trans = ttk.Label(self.window)

    def translate(self):
        text = self.test.get()
        translated_text = tr.translate_text(text, to_language='ru')
        self.trans.config(text=translated_text)

    def create_widgets(self):
        txt = ttk.Entry(self.window, textvariable=self.test)
        txt.pack(anchor='w', pady=45, fill='y')

        bt = ttk.Button(self.window, text='Translate', command=self.translate)
        bt.pack(anchor='s')

        self.trans.pack(anchor='s')

    def run(self):
        self.create_widgets()
        self.window.mainloop()

if __name__ == "__main__":
    translator = Translator()
    translator.run()

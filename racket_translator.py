# #
import tkinter
from googletrans import Translator
from tkinter import *
from tkinter import PhotoImage

translator = Translator()

tr_word = ''
word = ''


def add_window():
    root = tkinter.Tk()
    root.title("Racket Translator")
    root.geometry("500x350")
    root.resizable(False, False)
    root.config(bg="#060606")

    def lang():
        global word
        global tr_word
        word = rus_entry.get()
        l = translator.detect(text=word)
        if l.lang == 'ru':
            tr_word = translator.translate(word, dest='en').text
            return tr_word
        elif l.lang == 'en':
            tr_word = translator.translate(word, dest='ru').text
            return tr_word

    def tran():
        global word
        global tr_word
        word = rus_entry.get()
        lang()
        show_entry.insert(0, tr_word)
        rus_entry.delete(0, 'end')

    def clear():
        show_entry.delete(0, 'end')

    img = PhotoImage(file='enot.jpg')
    img_lbl = Label(root)
    img_lbl.image = img
    img_lbl['image'] = img_lbl.image
    img_lbl['bg'] = '#060606'
    img_lbl.place(relx=0.5, y=65, anchor='center')

    rus_entry = tkinter.Entry(root,
                              font="Lato 16",
                              bg="#03c4ff",
                              justify="center",
                              width=20)
    rus_entry.place(relx=0.5, y=170, anchor='center')

    rus_label = tkinter.Label(root,
                              text="введите текст",
                              font="Lato 13",
                              bg="#060606",
                              fg="#7C7C7C",
                              justify="center",
                              width=17)
    rus_label.place(relx=0.5, y=140, anchor='center')

    translator_btn = tkinter.Button(root,
                                    text="перевести",
                                    font="Lato 16",
                                    bg="#5e9c37",
                                    fg="#000000",
                                    activebackground="#99fe59",
                                    justify="center",
                                    borderwidth=0,
                                    width=30,
                                    command=tran
                                    )
    translator_btn.place(relx=0.5, y=220, anchor='center')

    show_entry = tkinter.Entry(root,
                               font="Lato 16 bold",
                               bg="#03c4ff",
                               fg="#000000",
                               justify="center",
                               width=30)
    show_entry.place(relx=0.5, y=270, anchor='center')

    clear_btn = tkinter.Button(root,
                               text="очистить",
                               font="Lato 16",
                               bg="#af0000",
                               fg="#000000",
                               activebackground="#ff0000",
                               justify="center",
                               borderwidth=0,
                               width=30,
                               command=clear
                               )
    clear_btn.place(relx=0.5, y=320, anchor='center')

    root.mainloop()


def main():
    # racketa_translate_en()
    # racketa_translate_ru()
    add_window()


if __name__ == '__main__':
    main()

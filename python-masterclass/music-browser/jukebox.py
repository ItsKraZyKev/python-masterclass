import sqlite3

try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter

conn = sqlite3.connect('music.db', )


class Scrollbox(tkinter.Listbox):

    def __init__(self, window, **kwargs):
        super().__init__(window, **kwargs)

        self.scrollbar = tkinter.Scrollbar(window, orient=tkinter.VERTICAL, command=self.yview)

    def grid(self, row, column, sticky='nsw', rowspan=1, columnspan=1, **kwargs):
        super().grid(row=row, column=column, sticky=sticky, rowspan=rowspan, columnspan=columnspan, **kwargs)
        self.scrollbar.grid(row=row, column=column, sticky='nse', rowspan=rowspan)
        self['yscrollcommand'] = self.scrollbar.set


main_window = tkinter.Tk()
main_window.title('Music DB Browser')
main_window.geometry('1024x768')

main_window.columnconfigure(0, weight=2)
main_window.columnconfigure(1, weight=2)
main_window.columnconfigure(2, weight=2)
main_window.columnconfigure(3, weight=1)  # spacer column on right

main_window.rowconfigure(0, weight=1)
main_window.rowconfigure(1, weight=5)
main_window.rowconfigure(2, weight=5)
main_window.rowconfigure(3, weight=1)

# ==== labels =====
tkinter.Label(main_window, text='Artists').grid(row=0, column=0)
tkinter.Label(main_window, text='Albums').grid(row=0, column=1)
tkinter.Label(main_window, text='Songs').grid(row=0, column=2)

# ==== Artists Listbox =====
artist_list = Scrollbox(main_window)
artist_list.grid(row=1, column=0, sticky='nsew', rowspan=2, padx=(30, 0))
artist_list.config(border=2, relief='sunken')

# ==== Albums Listbox =====
album_lv = tkinter.Variable(main_window)
album_lv.set(('Choose an artist',))
album_list = Scrollbox(main_window, listvariable=album_lv)
album_list.grid(row=1, column=1, sticky='nsew', padx=(30, 0))
album_list.config(border=2, relief='sunken')

# ==== Songs Listbox =====
song_lv = tkinter.Variable(main_window)
song_lv.set(('Choose an album',))
song_list = Scrollbox(main_window, listvariable=song_lv)
song_list.grid(row=1, column=2, sticky='nsew', padx=(30, 0))
song_list.config(border=2, relief='sunken')

# ==== Main loop =====
test_list = range(0, 101)
album_lv.set(tuple(test_list))
main_window.mainloop()
print('Closing database connection')
conn.close()

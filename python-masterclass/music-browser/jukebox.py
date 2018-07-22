import sqlite3

try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter

conn = sqlite3.connect('music.db', )


class Scrollbox(tkinter.Listbox):

    def __init__(self, window, **kwargs):
        super().__init__(window, exportselection=False, **kwargs)

        self.scrollbar = tkinter.Scrollbar(window, orient=tkinter.VERTICAL, command=self.yview)

    def grid(self, row, column, sticky='nsw', rowspan=1, columnspan=1, **kwargs):
        super().grid(row=row, column=column, sticky=sticky, rowspan=rowspan, columnspan=columnspan, **kwargs)
        self.scrollbar.grid(row=row, column=column, sticky='nse', rowspan=rowspan)
        self['yscrollcommand'] = self.scrollbar.set


class DataListBox(Scrollbox):

    def __init__(self, window, connection, table, field, sort_order=(), **kwargs):
        super().__init__(window, **kwargs)
        self.cursor = connection.cursor()
        self.table = table
        self.field = field

        self.sql_select = "SELECT " + self.field + ', _id' + ' FROM ' + self.table
        if sort_order:
            self.sql_sort = ' ORDER BY ' + ','.join(sort_order)
        else:
            self.sql_sort = ' ORDER BY ' + self.field

    def clear(self):
        self.delete(0, tkinter.END)

    def requery(self):
        print(self.sql_select + self.sql_sort)  # TODO delete this line
        self.cursor.execute(self.sql_select + self.sql_sort)

        # clear the listbox contents before reloading
        self.clear()
        for value in self.cursor:
            self.insert(tkinter.END, value[0])


def get_albums(event):
    lb = event.widget
    index = lb.curselection()[0]
    artist_name = lb.get(index),

    # get the artist ID from the database row
    artist_id = conn.execute('select artists._id from artists where artists.name=?', artist_name).fetchone()
    alist = []
    for row in conn.execute('select albums.name from albums where albums.artist = ? order by albums.name', artist_id):
        alist.append(row[0])
    album_lv.set(tuple(alist))
    song_lv.set(('Choose an album',))


def get_songs(event):
    lb = event.widget
    index = int(lb.curselection()[0])
    album_name = lb.get(index),

    # get the artist ID from the database row
    album_id = conn.execute('select albums._id from albums where albums.name=?', album_name).fetchone()
    alist = []
    for x in conn.execute('select songs.title from songs where songs.album = ? order by songs.track', album_id):
        alist.append(x[0])
    song_lv.set(tuple(alist))


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
artist_list = DataListBox(main_window, conn, 'artists', 'name')
artist_list.grid(row=1, column=0, sticky='nsew', rowspan=2, padx=(30, 0))
artist_list.config(border=2, relief='sunken')

artist_list.requery()
artist_list.bind('<<ListboxSelect>>', get_albums)

# ==== Albums Listbox =====
album_lv = tkinter.Variable(main_window)
album_lv.set(('Choose an artist',))
album_list = DataListBox(main_window, conn, 'albums', 'name', sort_order=('name',))
album_list.requery()
album_list.grid(row=1, column=1, sticky='nsew', padx=(30, 0))
album_list.config(border=2, relief='sunken')

album_list.bind('<<ListboxSelect>>', get_songs)
# ==== Songs Listbox =====
song_lv = tkinter.Variable(main_window)
song_lv.set(('Choose an album',))
song_list = DataListBox(main_window, conn, 'songs', 'title', ('track', 'title'))
song_list.requery()
song_list.grid(row=1, column=2, sticky='nsew', padx=(30, 0))
song_list.config(border=2, relief='sunken')

# ==== Main loop =====
main_window.mainloop()
print('Closing database connection')
conn.close()

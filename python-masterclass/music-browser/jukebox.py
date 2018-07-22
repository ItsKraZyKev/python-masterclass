import sqlite3

try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter


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

        self.linked_box = None
        self.link_field = None
        self.link_value = None

        self.cursor = connection.cursor()
        self.table = table
        self.field = field

        self.bind('<<ListboxSelect>>', self.on_select)

        self.sql_select = "SELECT " + self.field + ', _id' + ' FROM ' + self.table
        if sort_order:
            self.sql_sort = ' ORDER BY ' + ','.join(sort_order)
        else:
            self.sql_sort = ' ORDER BY ' + self.field

    def clear(self):
        self.delete(0, tkinter.END)

    def link(self, widget, link_field):
        self.linked_box = widget
        widget.link_field = link_field

    def requery(self, link_value=None):
        self.link_value = link_value  # store the id so we konw the "master" record we're populated from
        if link_value and self.link_field:
            sql = self.sql_select + ' where ' + self.link_field + '=?' + self.sql_sort
            self.cursor.execute(sql, (link_value,))
        else:
            self.cursor.execute(self.sql_select + self.sql_sort)

        # clear the listbox contents before reloading
        self.clear()
        for value in self.cursor:
            self.insert(tkinter.END, value[0])

        if self.linked_box:
            self.linked_box.clear()

    def on_select(self, event):
        if self.linked_box:
            index = self.curselection()[0]
            value = self.get(index),

            # get the ID from the database row
            # make sure we are getting the correct one. by including the link_value if appropriate
            if self.link_value:
                value = value[0], self.link_value
                sql_where = ' where ' + self.field + '=? AND ' + self.link_field + '=?'
            else:
                sql_where = ' where ' + self.field + '=?' \
                                                     ''
            link_id = self.cursor.execute(self.sql_select + sql_where, value).fetchone()[1]
            self.linked_box.requery(link_id)


if __name__ == '__main__':
    conn = sqlite3.connect('music.db', )

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

    # ==== Albums Listbox =====
    album_lv = tkinter.Variable(main_window)
    album_lv.set(('Choose an artist',))
    album_list = DataListBox(main_window, conn, 'albums', 'name', sort_order=('name',))
    album_list.grid(row=1, column=1, sticky='nsew', padx=(30, 0))
    album_list.config(border=2, relief='sunken')

    artist_list.link(album_list, 'artist')

    # ==== Songs Listbox =====
    song_lv = tkinter.Variable(main_window)
    song_lv.set(('Choose an album',))
    song_list = DataListBox(main_window, conn, 'songs', 'title', ('track', 'title'))
    song_list.grid(row=1, column=2, sticky='nsew', padx=(30, 0))
    song_list.config(border=2, relief='sunken')

    album_list.link(song_list, 'album')

    # ==== Main loop =====
    main_window.mainloop()
    print('Closing database connection')
    conn.close()

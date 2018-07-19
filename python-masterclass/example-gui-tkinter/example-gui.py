try:
    import tkinter
except ImportError:
    import Tkinter as tkinter
import os

main_window = tkinter.Tk()

main_window.title('Kev Program')
main_window.geometry('640x480+200+200')
main_window['padx'] = 8

label = tkinter.Label(main_window, text='Grid Demo')
label.grid(row=0, column=0, columnspan=3)

main_window.columnconfigure(0, weight=100)
main_window.columnconfigure(1, weight=1)
main_window.columnconfigure(2, weight=1000)
main_window.columnconfigure(3, weight=600)
main_window.columnconfigure(4, weight=1000)

main_window.rowconfigure(0, weight=1)
main_window.rowconfigure(1, weight=10)
main_window.rowconfigure(2, weight=1)
main_window.rowconfigure(3, weight=3)
main_window.rowconfigure(4, weight=3)

file_list = tkinter.Listbox(main_window)
file_list.grid(row=1, column=0, sticky='nsew', rowspan=2)
file_list.config(border=2, relief='sunken')
for zone in os.listdir('C://Program Files'):
    file_list.insert(tkinter.END, zone)

list_scroll = tkinter.Scrollbar(main_window, orient=tkinter.VERTICAL, command=file_list.yview)
list_scroll.grid(row=1, column=1, sticky='nsw', rowspan=2)
file_list['yscrollcommand'] = list_scroll.set

# frame for the radio buttons
option_frame = tkinter.LabelFrame(main_window, text='File Details')
option_frame.grid(row=1, column=2, sticky='ne')

rb_value = tkinter.IntVar()
rb_value.set(0)
# Radio Buttons
radio1 = tkinter.Radiobutton(option_frame, text='Filename', value=1, variable=rb_value)
radio2 = tkinter.Radiobutton(option_frame, text='Path', value=2, variable=rb_value)
radio3 = tkinter.Radiobutton(option_frame, text='Timestamp', value=3, variable=rb_value)
radio1.grid(row=0, column=0, sticky='w')
radio2.grid(row=1, column=0, sticky='w')
radio3.grid(row=2, column=0, sticky='w')

# Widget to display the result
result_label = tkinter.Label(main_window, text='Result')
result_label.grid(row=2, column=2, sticky='nw')
result = tkinter.Entry(main_window)
result.grid(row=2, column=2, sticky='sw')

# frame for the time spinners
time_frame = tkinter.LabelFrame(main_window, text='Time')
time_frame.grid(row=3, column=0, sticky='new')
# Time spinners
hour_spinner = tkinter.Spinbox(time_frame, width=2, values=tuple(range(0, 24)))
minute_spinner = tkinter.Spinbox(time_frame, width=2, from_=0, to=59)
second_spinner = tkinter.Spinbox(time_frame, width=2, from_=0, to=59)

hour_spinner.grid(row=0, column=0)
tkinter.Label(time_frame, text=':').grid(row=0, column=1)
minute_spinner.grid(row=0, column=2)
tkinter.Label(time_frame, text=':').grid(row=0, column=1)
second_spinner.grid(row=0, column=4)
time_frame['padx'] = 36

# FRame for the date spinners
date_frame = tkinter.Frame(main_window)
date_frame.grid(row=4, column=0, sticky='new')
# Date Lables
day_label = tkinter.Label(date_frame, text='Day')
month_label = tkinter.Label(date_frame, text='Month')
year_label = tkinter.Label(date_frame, text='Year')
day_label.grid(row=0, column=0, sticky='w')
month_label.grid(row=0, column=1, sticky='w')
year_label.grid(row=0, column=2, sticky='w')
# Date spinners
day_spin = tkinter.Spinbox(date_frame, width=5, from_=1, to=31)
month_spin = tkinter.Spinbox(date_frame, width=5, values=(
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
year_spin = tkinter.Spinbox(date_frame, width=5, from_=2000, to=2099)
day_spin.grid(row=1, column=0)
month_spin.grid(row=1, column=1)
year_spin.grid(row=1, column=2)

# Buttons
ok_button = tkinter.Button(main_window, text='OK')
cancel_button = tkinter.Button(main_window, text='Cancel', command=main_window.destroy)
ok_button.grid(row=4, column=3, sticky='e')
cancel_button.grid(row=4, column=4, sticky='w')

main_window.mainloop()

print(rb_value.get())

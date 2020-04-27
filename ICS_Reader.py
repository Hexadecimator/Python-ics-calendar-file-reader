import tkinter as tk
from tkinter import filedialog
import re

ics_filepath = "empty"

window = tk.Tk()
window.geometry('700x350')
window.title(".ICS File Viewer")

date_start_label = tk.Label(window, text = "Meeting Start: ")
date_start_label.grid(column = 4, row = 2)

date_start_data_label = tk.Label(window, text = "")
date_start_data_label.grid(column = 5, row = 2)

timezone_start_label = tk.Label(window, text = "Timezone: ")
timezone_start_label.grid(column = 6, row = 2)

timezone_start_data_label = tk.Label(window, text = "")
timezone_start_data_label.grid(column = 7, row = 2)

date_end_label = tk.Label(window, text = "Meeting End: ")
date_end_label.grid(column = 4, row = 3)

date_end_data_label = tk.Label(window, text = "")
date_end_data_label.grid(column = 5, row = 3)

timezone_end_label = tk.Label(window, text = "Timezone: ")
timezone_end_label.grid(column = 6, row = 3)

timezone_end_data_label = tk.Label(window, text = "")
timezone_end_data_label.grid(column = 7, row = 3)

greeting = tk.Label(window, text = "Select iCS file for viewing:")
greeting.grid(column = 4, row = 5)


def file_button_clicked(): 
    ics_filepath = filedialog.askopenfilename(initialdir = "C:/Users/Logan/Documents/Python Projects/ICS_Reader/ICS_Reader",
                                             title = "Select iCS File", 
                                             filetypes = (("iCS Files", "*.ics"),("All Files", "*.*")))

    if ics_filepath != "empty":
        file_object = open(ics_filepath, "r")

        found = "NA"
        for row in file_object:

            if "DTSTART;" in row:
                m = re.search('TZID="(.*?)"', row)
                if m:
                    found = m.group(0) 
                    found = found.replace('TZID="', "")
                    found = found.replace('"',"")
                    print(found)
                    timezone_start_data_label.configure(text=found)

                m = re.search('":[0-9]\w+', row)
                if m:
                    found = m.group(0)
                    found = found.replace('":',"")
                    print(found)
                    date_start_data_label.configure(text=found)

            if "DTEND;" in row:
                m = re.search('TZID="(.*?)"', row)
                if m:
                    found = m.group(0) 
                    found = found.replace('TZID="', "")
                    found = found.replace('"',"")
                    print(found)
                    timezone_end_data_label.configure(text=found)

                m = re.search('":[0-9]\w+', row)
                if m:
                    found = m.group(0)
                    found = found.replace('":',"")
                    print(found)
                    date_end_data_label.configure(text=found)




def main():

    btn = tk.Button(window, text = "Select File", command = file_button_clicked)
    btn.grid(column = 4, row = 6)

    window.mainloop()

main()

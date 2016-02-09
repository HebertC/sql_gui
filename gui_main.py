#!/usr/bin/env python
from tkinter import *
import sqlite3
import os
import tkinter as tk
# from tkinter import *
# from Tkinter import *

__author__ = 'clara @ mctc'

database_filename = "itec_2865_sql_injection_demo.db"


# Represents the GUI window.
class MenuGUI():

    def __init__(self):

        self.root = tk.Tk()
        self.root.title("GUI for store data")
        # set the variable
        self.window_height = 700

        self.sidebar_width = 200

        self.main_area_width = 700

        self.sidebar_bg_color = 'white'

        self.mainarea_bg_color = '#CCC'

        sidebar = tk.Frame(
            self.root, width = self.sidebar_width, bg = self.sidebar_bg_color, height = self.window_height, relief = 'sunken', borderwidth = 2)
        sidebar.pack(expand=True, fill='both', side = 'left', anchor = 'nw')

        # adding the buttons on the right side bar

        # adding the T shirt button on right side-bar
        # relx and rely are the attribute which set the postsion

        tshirt = tk.Button(self.root, text = "T-shirt", command=self._only_tshirt_show)

        tshirt.pack()

        tshirt.place(bordermode = OUTSIDE, height = 50, width = self.sidebar_width, relx=.0, rely=.001)

        # adding the Poster button on right side-bar
        # relx and rely are the attribute which set the postsion
        posters = tk.Button(self.root, text ="Posters")

        posters.pack()

        posters.place(bordermode = OUTSIDE, height = 50, width = self.sidebar_width,relx=.0, rely=.09)

        # adding the Boots button on right side-bar
        # relx and rely are the attribute which set the postsion

        boots = tk.Button(self.root, text ="Boots")

        boots.pack()

        boots.place(bordermode = OUTSIDE, height = 50, width = self.sidebar_width,relx=.0, rely=.179)

        self.mainarea_tshirt = tk.Frame(self.root, bg = self.mainarea_bg_color, width = self.main_area_width, height = self.window_height)

        self.mainarea_tshirt.pack(expand = True, fill = 'both', side = 'right')



        self.root.mainloop()

    """
    This mestod will hide all the displays and show only the
    t-shirt window
    """
    def _only_tshirt_show(self):
        self.mainarea_tshirt.destroy()
        self.mainarea_tshirt = tk.Frame(self.root, bg = self.mainarea_bg_color, width = self.main_area_width, height = self.window_height)

        self.mainarea_tshirt.pack(expand = True, fill = 'both', side = 'right')

        self.root.mainloop()


    def _only_posters_show(self):
        self.mainarea_tshirt.destroy()
        self.mainarea_boots.destroy()


    def _only_boot_show(self):
        self.mainarea_tshirt.destroy()
        self.mainarea_posters.destroy()

def setup_database():

    # checking the database file is exist
    # if the file is exist
    # remove the existing data and create the new database
    if os.path.isfile(database_filename):
        db = sqlite3.connect(database_filename)
        cursor = db.cursor()
        # Delete any existing data
        cursor.execute('DROP TABLE IF EXISTS users')
        print ("Existing Data are deleted")

    else:
        db = sqlite3.connect(database_filename)
        cursor = db.cursor()
        print ("New Database is created")

    # Create a database table with columns for user's name (name), user id (user),  and password (password)
    # add the id as integer primary so it will realte to the unique
    # indentifcation
    cursor.execute('''CREATE TABLE users
        (id INTEGER PRIMARY KEY ASC AUTOINCREMENT,
        username TEXT NOT NULL,
        name TEXT NOT NULL,
        password TEXT
        );'''
                   )

    # adding the custome data in sqlite
    cursor.execute("INSERT INTO users (username,name,password) \
      VALUES ('admin', 'Abby Admin','kittens')")
    cursor.execute("INSERT INTO users (username,name,password) \
      VALUES ('bill', 'Bill S Preston','excellent!')")
    cursor.execute("INSERT INTO users (username,name,password) \
      VALUES ('bart', 'Bart Simpson','eatmyshorts')")
    cursor.execute("INSERT INTO users (username,name,password) \
      VALUES ('miley', 'Miley Cyrus','top40')")
    cursor.execute("INSERT INTO users (username,name,password) \
      VALUES ('Hebert', 'Joshep','Skywalker')")
    db.commit()
    db.close()
    print ("Example Data is Entered")


def start_gui():

    MenuGUI().mainloop()


def quit():

    sys.exit()


def main():
    setup_database()
    start_gui()


if __name__ == '__main__':
    main()
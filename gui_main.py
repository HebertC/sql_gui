#!/usr/bin/env python

from tkinter import *
import sqlite3
import os
import tkinter as tk



# Represents the GUI window.
class MenuGUI():

    def __init__(self):

        self.root = tk.Tk()
        self.root.title("GUI for store data")
        # set the variable
        self.window_height = 500

        self.sidebar_width = 200

        self.main_area_width = 400

        self.sidebar_bg_color = 'gray'

        self.mainarea_bg_color = 'white'

        # calling the sidebar method
        self._set_sidebar()

        # initialize the frames with empty everything
        self.mainarea_tshirt = tk.Frame(self.root)

        self.mainarea_posters = tk.Frame(self.root)

        self.mainarea_boots = tk.Frame(self.root)

        # calling the frame to show initially
        self._only_tshirt_show()


    def _set_sidebar(self):

        sidebar = tk.Frame(
            self.root, width = self.sidebar_width, bg = self.sidebar_bg_color, height =self.window_height,
            relief='sunken', borderwidth = 5)

        sidebar.pack(expand=True, fill='both', side = 'left', anchor = 'nw')

        # adding the T shirt button on right side-bar
        # relx and rely are the attribute which set the postilion

        tshirt = tk.Button(self.root, text = "T-shirt", command=self._only_tshirt_show)

        tshirt.pack()

        tshirt.place(bordermode = OUTSIDE, height = 50, width = self.sidebar_width, relx=.03, rely=.013)

        # adding the Poster button on right side-bar
        # relx and rely are the attribute which set the postsion
        posters = tk.Button(self.root, text ="Posters", command=self._only_posters_show)

        posters.pack()

        posters.place(bordermode = OUTSIDE, height = 50, width = self.sidebar_width,relx=.03, rely=.11)

        # adding the Boots button on right side-bar
        # relx and rely are the attribute which set the postsion

        boots = tk.Button(self.root, text ="Boots", command=self._only_boot_show)

        boots.pack()

        boots.place(bordermode = OUTSIDE, height = 50, width = self.sidebar_width,relx=.03, rely=.21)


    """
    This method will hide all the displays and show only the
    t-shirt window
    """
    def _only_tshirt_show(self):

        """
        Below line destroy the all frames
        """

        # destroy the all frames
        self.mainarea_tshirt.destroy()

        self.mainarea_posters.destroy()

        self.mainarea_boots.destroy()

        self.root.update()

        self.root.minsize(self.main_area_width,self.window_height)

        self.mainarea_tshirt = tk.Frame(self.root, bg = self.mainarea_bg_color,
                                        width = self.main_area_width, height = self.window_height)

        self.mainarea_tshirt.pack(expand = True, fill = 'both', side = 'right' )

        Label(self.mainarea_tshirt, text="T-Shirt Name").pack()

        self._storeVar = StringVar()
        self._tablename = "tshirts"

        # adding the Entry (text-field) on frame
        # adding the button on the text field
        # command attribute in button will execute the method or command

        Entry(self.mainarea_tshirt, textvariable=self._storeVar, width=15).pack()

        Button(self.mainarea_tshirt, text="Enter",width=15, command=self._enter_data).pack()

        self.root.mainloop()

    """
    This mestod will hide all the displays and show only the
    Posters window
    """
    def _only_posters_show(self):

        # destroy the all frames
        self.mainarea_tshirt.destroy()

        self.mainarea_posters.destroy()

        self.mainarea_boots.destroy()


        self.root.update()

        self.root.minsize(self.main_area_width,self.window_height)

        self.mainarea_posters = tk.Frame(self.root, bg = self.mainarea_bg_color,
                                         width = self.main_area_width, height = self.window_height)

        self.mainarea_posters.pack(expand = True, fill = 'both', side = 'right')

        Label(self.mainarea_posters, text="Poster Name").pack()

        self._storeVar = StringVar()
        self._tablename = "posters"

        # adding the Entry (text-field) on frame
        # adding the button on the text field
        # command attribute in button will execute the method or command

        Entry(self.mainarea_posters, textvariable=self._storeVar, width=15).pack()

        Button(self.mainarea_posters, text="Enter",width=15, command=self._enter_data).pack()

        self.root.mainloop()


    """
    This method will hide all the displays and show only the
    Boot window
    """
    def _only_boot_show(self):

        # destroy the all frames
        self.mainarea_tshirt.destroy()
        self.mainarea_posters.destroy()
        self.mainarea_boots.destroy()

        self.root.update()

        self.root.minsize(self.main_area_width,self.window_height)

        self.mainarea_boots = tk.Frame(self.root, bg = self.mainarea_bg_color, width = self.main_area_width, height = self.window_height)

        self.mainarea_boots.pack(expand = True, fill = 'both', side = 'right')

        Label(self.mainarea_boots, text="Boot Name").pack()

        self._storeVar = StringVar()
        self._tablename = "boots"

        # adding the Entry (text-field) on frame
        # adding the button on the text field
        # command attribute in button will execute the method or command
        Entry(self.mainarea_boots, textvariable=self._storeVar, width=15).pack()

        Button(self.mainarea_boots, text="Enter",width=15, command=self._enter_data).pack()

        self.root.mainloop()

    """
    This method call when the button the side-bar is clicked
    This method get the values from the "Entry" widget and
    insert in the database
    """
    def _enter_data(self):
        storeVar = self._storeVar.get()
        db = sqlite3.connect("database_filename")
        cursor = db.cursor()
        cursor.execute('insert into %s (name) values (?)'%self._tablename, (storeVar,))
        db.commit()
        """
        select data from the database and show them
        on the console.
        """
        for row in cursor.execute('SELECT * FROM %s'%self._tablename):
            print(row)
        db.close()



def setup_database():

    # checking the database file is exist
    # if the file is exist
    # remove the existing data and create the new database
    if os.path.isfile("database_filename"):
        db = sqlite3.connect("database_filename")
        cursor = db.cursor()
        # Delete any existing data
        cursor.execute('DROP TABLE IF EXISTS tshirts')
        cursor.execute('DROP TABLE IF EXISTS posters')
        cursor.execute('DROP TABLE IF EXISTS boots')

        print ("Existing Data are deleted")

    else:
        db = sqlite3.connect("database_filename")
        cursor = db.cursor()
        print ("New Database is created")

    # Create a database table
    # add the id as integer primary so it will relate to the unique
    # identification
    cursor.execute('''CREATE TABLE tshirts
        (id INTEGER PRIMARY KEY ASC AUTOINCREMENT,
        name TEXT NOT NULL
        );''');
    cursor.execute('''CREATE TABLE posters
        (id INTEGER PRIMARY KEY ASC AUTOINCREMENT,
        name TEXT NOT NULL
        );''');
    cursor.execute('''CREATE TABLE boots
        (id INTEGER PRIMARY KEY ASC AUTOINCREMENT,
        name TEXT NOT NULL
        );''');

    db.commit()
    db.close()
    print ("Tables are created")


def start_gui():

    MenuGUI().mainloop()


def quit():

    sys.exit()


def main():
    setup_database()
    start_gui()


if __name__ == '__main__':
    main()
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
        self.main_area_width = 700
        self.sidebar_bg_color = 'gray'
        self.mainarea_bg_color = 'white'
        # calling the sidebar method
        self._set_sidebar()
        # initialize the frames with empty everything
        self.mainarea_tshirt = tk.Frame(self.root)
        self.mainarea_posters = tk.Frame(self.root)
        self.mainarea_boots = tk.Frame(self.root)
        self.mainarea_boots = tk.Frame(self.root)
        self.mainarea_show_all_items = tk.Frame(self.root)
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
        # relx and rely are the attribute which set the position
        posters = tk.Button(self.root, text ="Posters", command=self._only_posters_show)

        posters.pack()

        posters.place(bordermode = OUTSIDE, height = 50, width = self.sidebar_width,relx=.03, rely=.12)

        # adding the Boots button on right side-bar
        # relx and rely are the attribute which set the position

        boots = tk.Button(self.root, text ="Boots", command=self._only_boot_show)

        boots.pack()

        boots.place(bordermode = OUTSIDE, height = 50, width = self.sidebar_width,relx=.03, rely=.225)

        """
        adding the menu in the sidebar which will show
        the item stored in the database
        on the click event this will call the _show_all_items function
        please the function _show_all_items definition for more detail
        """
        show_items = tk.Button(self.root, text ="Show All Items", command=self._show_all_items)

        show_items.pack()

        show_items.place(bordermode = OUTSIDE, height = 50, width = self.sidebar_width,relx=.03, rely=.333)


        # adding the Exit button on Left side-bar
        # relx and rely are the attribute which set the position

        exit = tk.Button(self.root, text ="Exit", command=quit)

        exit.pack()

        exit.place(bordermode = OUTSIDE, height = 50, width = self.sidebar_width,relx=.03, rely=.86)


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
        self.mainarea_show_all_items.destroy()

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

        self.entry_mainarea_tshirt = Entry(self.mainarea_tshirt, textvariable=self._storeVar, width=15)
        self.entry_mainarea_tshirt.pack()

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
        self.mainarea_show_all_items.destroy()


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

        self.entry_mainarea_posters = Entry(self.mainarea_posters, textvariable=self._storeVar, width=15)
        self.entry_mainarea_posters.pack()

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
        self.mainarea_show_all_items.destroy()

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
        self.entry_mainarea_boots = Entry(self.mainarea_boots, textvariable=self._storeVar, width=15)
        self.entry_mainarea_boots.pack()
        Button(self.mainarea_boots, text="Enter",width=15, command=self._enter_data).pack()

        self.root.mainloop()

    """
    This method will invoke when the
    Show All Items button is clicked
    This method will do these steps
    - close all the frames and show only the
    Show All Items frame
    -
    """

    def _show_all_items(self):

        # destroy all the frames
        self.mainarea_tshirt.destroy()
        self.mainarea_posters.destroy()
        self.mainarea_boots.destroy()
        self.mainarea_show_all_items.destroy()
        self.root.update()

        self.root.minsize(self.main_area_width,self.window_height)

        self.mainarea_show_all_items = tk.Frame(self.root, bg = self.mainarea_bg_color, width = self.main_area_width, height = self.window_height)

        self.mainarea_show_all_items.pack(expand = True, fill = 'both', side = 'right')

        # adding the label with the text "All T-shirts"
        tshirt_string = StringVar()
        Label(self.mainarea_show_all_items, textvariable=tshirt_string, width=18).pack()
        tshirt_string.set("All T-shirts\n ===========================")
        self._get_all_data("tshirts")
        # adding the label with the text "All Posters"
        poster_string = StringVar()
        Label(self.mainarea_show_all_items, textvariable=poster_string, width=18).pack()
        poster_string.set("\n\nAll Poster\n ==============================")
        self._get_all_data("posters")
        # adding the label with the text "All Boots"
        boots_string = StringVar()
        Label(self.mainarea_show_all_items, textvariable=boots_string, width=18).pack()
        boots_string.set("\n\n All Boots\n =============================")
        self._get_all_data("boots")



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
        # Empty the ENTRY widget
        if self._tablename == "tshirts":
            self.entry_mainarea_tshirt.delete(0, 'end')
        elif self._tablename == "boots":
            self.entry_mainarea_boots.delete(0, 'end')
        else:
            self.entry_mainarea_posters.delete(0, 'end')


        """
        select data from the database and show them
        on the console.
        """
        for row in cursor.execute('SELECT * FROM %s'%self._tablename):
            print(row)
        db.close()

    """
    get the all data from database
    """
    def _get_all_data(self, tbl_name):
        print (tbl_name)
        db = sqlite3.connect("database_filename")
        cursor = db.cursor()
        """
        select data from the database with the count and show them
        on the label.
        count and group by in this query calculate the distinct values
        in the table
        later in the loop these values assign to the Label
        """
        for row in cursor.execute('SELECT name, count(name) FROM %s group by name'%tbl_name):
            all_item_string = StringVar()
            Label(self.mainarea_show_all_items, textvariable=all_item_string, width=18,justify=CENTER).pack()
            string= str(row[0]) +" ---- "+str(row[1])
            all_item_string.set(string)
            print (row)
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
    # this will add the name of the item
    # and will update the entry of no of items
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

    """
    adding the initial data
    """
    cursor.execute('''INSERT INTO tshirts(name) VALUES('Broncos');''');
    cursor.execute('''INSERT INTO tshirts(name) VALUES('Chiefs');''');
    cursor.execute('''INSERT INTO tshirts(name) VALUES('Riders');''');
    cursor.execute('''INSERT INTO tshirts(name) VALUES('Cardinals');''');
    cursor.execute('''INSERT INTO tshirts(name) VALUES('Vikings');''');
    cursor.execute('''INSERT INTO tshirts(name) VALUES('Eagles');''');
    cursor.execute('''INSERT INTO posters(name) VALUES('Bears');''');
    cursor.execute('''INSERT INTO posters(name) VALUES('Steelers');''');
    cursor.execute('''INSERT INTO posters(name) VALUES('Browns');''');
    cursor.execute('''INSERT INTO posters(name) VALUES('Packers');''');
    cursor.execute('''INSERT INTO boots(name) VALUES('Bengals');''');
    cursor.execute('''INSERT INTO boots(name) VALUES('Panthers');''');


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
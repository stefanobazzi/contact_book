#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PySide.QtGui import QApplication, QMainWindow
from contact_book_gui import Ui_ContactBookGui
from contact_book_data import Contacts, User

class MainWindow(QMainWindow, Ui_ContactBookGui):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        # Setup data
        self.contacts = Contacts()
        self.contacts.init_db()
        # Setup GUI
        self.setupUi(self)
        self.insert_button.clicked.connect(self.insert)
        self.search_button.clicked.connect(self.search)

    def insert(self):
        user = User(self.name_line.text(), self.surname_line.text(), 
            self.jobs_combo.currentText())
        self.contacts.add_contact(user)
        print(user.name, user.surname, user.job)

    def search(self):
        users = self.contacts.search_contact(self.name_line.text())


def main():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exec_()

if __name__ == '__main__':
    main()

#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PySide.QtGui import QApplication, QMainWindow, QTableWidgetItem
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
        self.viewall_button.clicked.connect(self.view_all)

    def insert(self):
        user = User(self.name_line.text(), self.surname_line.text(), 
            self.jobs_combo.currentText())
        self.contacts.add_contact(user)

    def create_rows(self, users):
        self.users_table.setRowCount(len(users))
        for i in range(len(users)):
            name = QTableWidgetItem(users[i].name)
            surname = QTableWidgetItem(users[i].surname)
            job = QTableWidgetItem(users[i].job)
            self.users_table.setItem(i, 0, name)
            self.users_table.setItem(i, 1, surname)
            self.users_table.setItem(i, 2, job)

    def search(self):
        users = self.contacts.search_contact(self.name_line.text())


def main():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exec_()

if __name__ == '__main__':
    main()

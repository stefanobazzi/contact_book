# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'contact_book_gui.ui'
#
# Created: Sun Jul 12 18:08:42 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ContactBookGui(object):
    def setupUi(self, ContactBookGui):
        ContactBookGui.setObjectName("ContactBookGui")
        ContactBookGui.resize(357, 423)
        self.insert_button = QtGui.QPushButton(ContactBookGui)
        self.insert_button.setGeometry(QtCore.QRect(30, 160, 87, 27))
        self.insert_button.setObjectName("insert_button")
        self.search_button = QtGui.QPushButton(ContactBookGui)
        self.search_button.setGeometry(QtCore.QRect(130, 160, 87, 27))
        self.search_button.setObjectName("search_button")
        self.name_line = QtGui.QLineEdit(ContactBookGui)
        self.name_line.setGeometry(QtCore.QRect(70, 30, 241, 31))
        self.name_line.setObjectName("name_line")
        self.jobs_combo = QtGui.QComboBox(ContactBookGui)
        self.jobs_combo.setGeometry(QtCore.QRect(70, 110, 241, 31))
        self.jobs_combo.setObjectName("jobs_combo")
        self.jobs_combo.addItem("")
        self.jobs_combo.addItem("")
        self.jobs_combo.addItem("")
        self.surname_line = QtGui.QLineEdit(ContactBookGui)
        self.surname_line.setGeometry(QtCore.QRect(70, 70, 241, 31))
        self.surname_line.setObjectName("surname_line")
        self.name_label = QtGui.QLabel(ContactBookGui)
        self.name_label.setGeometry(QtCore.QRect(10, 40, 58, 21))
        self.name_label.setObjectName("name_label")
        self.surname_label = QtGui.QLabel(ContactBookGui)
        self.surname_label.setGeometry(QtCore.QRect(10, 80, 58, 21))
        self.surname_label.setObjectName("surname_label")
        self.job_label = QtGui.QLabel(ContactBookGui)
        self.job_label.setGeometry(QtCore.QRect(10, 120, 58, 17))
        self.job_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.job_label.setObjectName("job_label")
        self.users_table = QtGui.QTableWidget(ContactBookGui)
        self.users_table.setGeometry(QtCore.QRect(30, 210, 301, 191))
        self.users_table.setAutoFillBackground(False)
        self.users_table.setRowCount(0)
        self.users_table.setColumnCount(3)
        self.users_table.setObjectName("users_table")
        self.users_table.setColumnCount(3)
        self.users_table.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.users_table.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.users_table.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.users_table.setHorizontalHeaderItem(2, item)
        self.viewall_button = QtGui.QPushButton(ContactBookGui)
        self.viewall_button.setGeometry(QtCore.QRect(240, 160, 87, 27))
        self.viewall_button.setObjectName("viewall_button")

        self.retranslateUi(ContactBookGui)
        QtCore.QMetaObject.connectSlotsByName(ContactBookGui)

    def retranslateUi(self, ContactBookGui):
        ContactBookGui.setWindowTitle(QtGui.QApplication.translate("ContactBookGui", "Contact Book", None, QtGui.QApplication.UnicodeUTF8))
        self.insert_button.setText(QtGui.QApplication.translate("ContactBookGui", "Insert", None, QtGui.QApplication.UnicodeUTF8))
        self.search_button.setText(QtGui.QApplication.translate("ContactBookGui", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.jobs_combo.setItemText(0, QtGui.QApplication.translate("ContactBookGui", "Engineer", None, QtGui.QApplication.UnicodeUTF8))
        self.jobs_combo.setItemText(1, QtGui.QApplication.translate("ContactBookGui", "Doctor", None, QtGui.QApplication.UnicodeUTF8))
        self.jobs_combo.setItemText(2, QtGui.QApplication.translate("ContactBookGui", "Tester", None, QtGui.QApplication.UnicodeUTF8))
        self.name_label.setText(QtGui.QApplication.translate("ContactBookGui", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.surname_label.setText(QtGui.QApplication.translate("ContactBookGui", "Surname", None, QtGui.QApplication.UnicodeUTF8))
        self.job_label.setText(QtGui.QApplication.translate("ContactBookGui", "Job", None, QtGui.QApplication.UnicodeUTF8))
        self.users_table.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("ContactBookGui", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.users_table.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("ContactBookGui", "Surname", None, QtGui.QApplication.UnicodeUTF8))
        self.users_table.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("ContactBookGui", "Job", None, QtGui.QApplication.UnicodeUTF8))
        self.viewall_button.setText(QtGui.QApplication.translate("ContactBookGui", "View all", None, QtGui.QApplication.UnicodeUTF8))


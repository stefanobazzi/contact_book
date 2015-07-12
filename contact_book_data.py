#! /usr/bin/env python
# -*- coding: utf-8 -*-

from os import getcwd
from os.path import exists 
import sqlite3

class User(object):

    def __init__(self, name, surname, job):
        self.name = name
        self.surname = surname
        self.job = job


class Contacts(object):

    def __init__(self):
        self.users = []
        self.db = None

    def init_db(self):
        """Create a new sqlite DB if not exits else load data"""
        if exists(getcwd()+'/data.db'):
            self.db = sqlite3.connect('data.db')
            users = self.db.execute("SELECT * FROM users").fetchall()
            self.users = [User(u[0], u[1], u[2]) for u in users]
        else:
            self.db = sqlite3.connect('data.db')
            self.db.execute(
                "CREATE TABLE users (name text, surname, text, job text)")
        self.db.close()

    def add_contact(self, user):
        self.users.append(user)
        self.db = sqlite3.connect('data.db')
        self.db.execute(
            "INSERT INTO users(name, surname, job) VALUES (?, ?, ?)", (user.name, user.surname, user.job))
        self.db.commit()
        self.db.close()

    def search_contact(self, name, surname=None, job=None):
        user_list = [u for u in self.users if u.name == name]
        return user_list

import datetime

from peewee import *

import forms

DATABASE = SqliteDatabase('journal.db')


class Post(Model):
    title = TextField()
    date = TextField()
    time_spent = TextField()
    content = TextField()
    resources = TextField()

    class Meta:
        database = DATABASE
        order_by = ('-timestamp',)


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Post], safe=True)
    DATABASE.close()

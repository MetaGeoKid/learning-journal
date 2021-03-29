import datetime

from peewee import *

DATABASE = SqliteDatabase('journal.db')


class Post(Model):
    title = TextField()
    date = DateField(default=datetime.datetime.now)
    time_spent = IntegerField()
    content = TextField()
    resources = TextField()

    class Meta:
        database = DATABASE
        order_by = ('-timestamp',)


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Post], safe=True)
    DATABASE.close()

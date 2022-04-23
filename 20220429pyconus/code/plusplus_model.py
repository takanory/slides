from peewee import SqliteDatabase, Model, CharField, IntegerField

db = SqliteDatabase("plusplus.db")

class Plusplus(Model):
    name = CharField(primary_key=True)  # fields
    counter = IntegerField(default=0)

    class Meta:
        database = db

db.connect()
db.create_tables([Plusplus], safe=True)

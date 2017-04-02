from mongoengine import *
class Person(Document):
    name = StringField()
    age = IntField()

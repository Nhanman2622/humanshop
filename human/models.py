from django.db import models

# Create your models here.
from mongoengine import *
class products(Document):
    name = StringField(required=True)
    writer = StringField()
    updatetime = IntField()
    content=StringField()
    img=StringField()
    status= IntField()
    slug= StringField()
    cost= IntField()

class Thems(Document):
    name = StringField(required=True)
    img=StringField(required=True)
    link=StringField(required=True)


from mongoengine import Document, StringField, IntField

class Product(Document):
    name = StringField(required=True, max_length=200)
    price = IntField(required=True, min_value=0)
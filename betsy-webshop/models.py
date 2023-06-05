# Models go here

from peewee import *

database = SqliteDatabase("betsy.db")


class BaseModel(Model):
    class Meta:
        database = database


class User(BaseModel):
    name = CharField()
    address = CharField()
    billing_info = CharField()


class Product(BaseModel):
    name = CharField()
    description = TextField()
    price = DecimalField(decimal_places=2)
    quantity = IntegerField()
    user = ForeignKeyField(User, backref="products")


class Tag(BaseModel):
    name = CharField(unique=True)
    products = ManyToManyField(Product, backref="tags")


class Transaction(BaseModel):
    buyer = ForeignKeyField(User, backref="transactions")
    product = ForeignKeyField(Product)
    quantity = IntegerField()


class initialize_database():
    with database:
        database.create_tables([User, Product, Tag, Transaction, Product.tags.get_through_model()])
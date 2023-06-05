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


class ProductTag(BaseModel):
    product = ForeignKeyField(Product)
    tag = ForeignKeyField(Tag)


class Transaction(BaseModel):
    buyer = ForeignKeyField(User, backref="transactions")
    product = ForeignKeyField(Product)
    quantity = IntegerField()


def initialize_database():
    with database:
        database.create_tables([User, Product, Tag, ProductTag, Transaction])


def populate_test_database():
    with database.atomic():
        # Example Users
        user1 = User.create(name="Johnny", address="Houthalenstraat 88", billing_info="Credit Card")
        user2 = User.create(name="Natascha", address="Leo Smitstraat 30", billing_info="IDEAL")
        user3 = User.create(name="Zakaria", address="ZuidAs 456", billing_info="PayPal")
        user4 = User.create(name="Jackson", address="Assumaburg 96", billing_info="Bitcoin")

        # Example Products
        product1 = Product.create(name="Cap", description="Knitted Baseball Cap", price=9.99, quantity=10, user=user1)
        product2 = Product.create(name="Sweater", description="Knitted Winter Sweater", price=19.99, quantity=3, user=user2)
        product3 = Product.create(name="Scarf", description="Gucci Scarf", price=24.99, quantity=5, user=user3)
        product4 = Product.create(name="Baseball", description="Signed Baseball", price=49.99, quantity=1, user=user4)

        # Example Tags
        tag_names = ["Clothing", "Winter", "Accessories"]
        tags = []
        for name in tag_names:
            try:
                tag = Tag.create(name=name)
            except IntegrityError:
                tag = Tag.get(name=name)
            tags.append(tag)

        # Associate tags with products
        for tag in tags:
            ProductTag.create(product=product1, tag=tag)
            ProductTag.create(product=product2, tag=tag)
            ProductTag.create(product=product3, tag=tag)
            ProductTag.create(product=product4, tag=tag)


if __name__ == "__main__":
    initialize_database()
    populate_test_database()

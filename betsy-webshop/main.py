# Do not modify these lines
__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

# Add your code after this line

from models import *


def search(term):
    return Product.select().where(
        (fn.Lower(Product.name).contains(term.lower())) |
        (fn.Lower(Product.description).contains(term.lower())))


def list_user_products(user_id):
    return  Product.select().where(Product.user_id == user_id)


def list_products_per_tag(tag_id):
    return Product.select().join(Product.tags.get_through_model()).where(Tag.id == tag_id)


def add_product_to_catalog(user_id, product):
    try:
        with database.atomic():
            user = User.get(User.id == user_id)
            new_product = Product.create(
                name=product["name"],
                description=product["description"],
                price=product["price"],
                quantity=product["quantity"],
                user=user
            )
            if "tags" in product:
                for tag_name in product["tags"]:
                    tag, _ = Tag.get_or_create(name=tag_name)
                    new_product.tags.add(tag)
        return True
    except IntegrityError:
        return False


def update_stock(product_id, new_quantity):
    try:
        product = Product.get(Product.id == product_id)
        product.quantity = new_quantity
        product.save()
        return True
    except DoesNotExist:
        return False


def purchase_product(product_id, buyer_id, quantity):
    try:
        with database.atomic():
            product = Product.get(Product.id == product_id)
            buyer = User.get(User.id == buyer_id)
            if product.quantity >= quantity:
                product.quantity -= quantity
                product.save()
                Transaction.create(buyer=buyer, product=product, quantity=quantity)
                return True
            else:
                return False
    except DoesNotExist:
        return False


def remove_product(product_id):
    try:
        product = Product.get(Product.id == product_id)
        product.delete.instance()
        return True
    except DoesNotExist:
        return False




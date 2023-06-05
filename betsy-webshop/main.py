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


def run_tests():
    # Search for products based on a term
    search_results = search("sweater")
    print("Search Results:")
    for product in search_results:
        print(f"- {product.name}")

    # View the products of a given user
    user_products = list_user_products(1)
    print("\nUser Products:")
    for product in user_products:
        print(f"- {product.name}")

    # View all products for a given tag
    tag_products = list_products_per_tag(1)
    print("\nTag Products:")
    for product in tag_products:
        print(f"- {product.name}")

    # Add a product to a user
    product = {
        "name": "Gloves",
        "description": "Warm gloves for winter",
        "price": 9.99,
        "quantity": 7,
        "tags": ["Accessories", "Winter"]
    }
    added = add_product_to_catalog(2, product)
    if added:
        print("\nProduct added successfully")
    else:
        print("\nFailed to add product")

    # Remove a product from a user
    removed = remove_product(2)
    if removed:
        print("\nProduct removed successfully")
    else:
        print("\nFailed to remove product")

    # Update the stock quantity of a product
    updated = update_stock(1, 15)
    if updated:
        print("\nStock quantity updated successfully")
    else:
        print("\nFailed to update stock quantity")

    # Handle a purchase between a buyer and a seller for a given product
    purchased = purchase_product(1, 2, 2)
    if purchased:
        print("\nProduct purchased successfully")
    else:
        print("\nFailed to purchase product")


if __name__ == "__main__":
    initialize_database()
    populate_test_database()
    run_tests()
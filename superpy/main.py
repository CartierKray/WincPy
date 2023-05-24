# Imports
import os
import argparse
import csv
from datetime import date

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"

# Your code below this line.
def main():
    parser = argparse.ArgumentParser(description="SuperPy - Supermarket Inventory Tool")

    # Add command-line arguments for different operations
    subparsers = parser.add_subparsers(dest="command")

    # Command for buying
    buy_parser = subparsers.add_parser("buy", help="Buy a product")
    buy_parser.add_argument("--product-name", required=True, help="Name of the product")
    buy_parser.add_argument("--product-price", required=True, help="Price of the product")
    buy_parser.add_argument("--expiration-date", required=True, help="Expiration date of the product")

    # Command for selling
    sell_parser = subparsers.add_parser("selling", help="Selling a product")
    sell_parser.add_argument("--product-name", required=True, help="Name of the product")
    sell_parser.add_argument("--product-price", required=True, help="Price of the product")

    # Report command
    report_parser = subparsers.add_parser("report", help="Generate reports")
    report_parser.add_argument("type", choices=["inventory", "revenue", "profit"], help="Type of report to generate")
    report_parser.add_argument("--date", help="Specify a specific date for the report")

    # Advance time command
    parser.add_argument("--advanced-time", type=int, help="The perceived date by a number of days")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Perform actions based on the provided arguments
    if args.command == "buy":
        # Implement the buying logic
        product_name = args.product_name
        product_price = args.product_price
        expiration_date = args.expiration_date
        buy_product(product_name, product_price, expiration_date)

    elif args.command == "selling":
        # Implement the selling logic
        product_name = args.product_name
        product_price = args.product_price
        sell_product(product_name, product_price)

    elif args.command == "report":
        # Implement generating reports logic
        report_type = args.type
        report_date = args.date
        generate_report(report_type, report_date)

    # Implement the logic for advancing the time
    if args.advanced_time:
        advance_time(args.advanced_time)


def buy_product(product_name, product_price, expiration_date):
    # Read the last ID from the bought.csv data file
    with open("bought.csv", "r") as file:
        reader = csv.reader(file)
        last_id = max(int(row[0]) for row in reader) if any(reader) else 0

    # Increment the ID for new purchase
    bought_id = last_id + 1

    # Get the current date
    current_date = date.today().strftime("%Y-%m-%d")

    # Append the purchase data to bought.csv data file
    with open("bought.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([bought_id, product_name, product_price, current_date, expiration_date])

    print("OK")

def sell_product(product_name, product_price):
    # Read the available stock from the bought.csv data file
    with open("bought.csv", "r") as file:
        reader = csv.reader(file)
        rows = list(reader)

    # Find the product in the stock
    for row in rows:
        if row[1] == product_name:
            bought_id = row[0]
            expiration_date = row[4]

            # remove the product from the stock
            rows.remove(row)

            # Append the sale data to sold.csv data file
            sold_data = [get_sale_id(), bought_id, get_current_date(), product_price]
            with open("sold.csv", "a", newline="") as sold_file:
                sold_writer = csv.writer(sold_file)
                sold_writer.writerow(sold_data)

            print("OK")
            break
    else:
        print("ERROR: Product not in stock")

def generate_report(report_type, report_date):
    # Implement the logic for generating reports
    print("Generating report:", report_type)
    if report_date:
        print("Date:", report_date)

def advance_time(days):
    # Implement the logic for advancing the time by the given number of days
    print("Advancing time by", days, "days")

def get_sale_id():
    # Placeholder code to generate a unique sale ID
    return "SALE-123"


def get_current_date():
    # Placeholder code to get the current date
    return date.today().strftime("%Y-%m-%d")


if __name__ == "__main__":
    main()


# ----------------------------------------------------------- #
 

"""
# Check if bought.csv file exists
if os.path.exists("bought.csv"):
    print("bought.csv file exists")
else:
    print("bought.csv file does not exist")

# Check if sold.csv file exists
if os.path.exists("sold.csv"):
    print("sold.csv file exists")
else:
    print("sold.csv file does not exist")

# Check the directory 
print("Current working directory:", os.getcwd())
"""
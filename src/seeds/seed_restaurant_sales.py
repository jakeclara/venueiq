# adds random restaurant sales to the database

from datetime import date
import random
from src.models.restaurant_sale import RestaurantSale
from src.models.menu_item import MenuItem
from src.seeds import seed_constants as sc

def make_restaurant_sale(sales_date: date, menu_item: MenuItem) -> RestaurantSale | None:
    """
    Create a RestaurantSale for a given date and menu item with a random quantity.

    If the generated quantity is 0, no sale is created and the function returns None.

    Args:
        sales_date (date): The date for which the sale should be generated.
        menu_item (MenuItem): The menu item being sold.

    Returns:
        RestaurantSale | None: A MongoEngine RestaurantSale document with randomized quantity,
        or None if no sale should be created for this item.
    """
    
    if menu_item.category == "Food":
        quantity = random.randint(sc.MIN_QTY_SOLD, sc.MAX_FOOD_QTY_SOLD)
    else:
        quantity = random.randint(sc.MIN_QTY_SOLD, sc.MAX_BEV_QTY_SOLD)

    if quantity == 0:
        return None

    sale = RestaurantSale(
        sales_date=sales_date,
        item=menu_item,
        category=menu_item.category,
        quantity=quantity
    )

    return sale


def seed_restaurant_sales() -> None:
    """
    Seed the database with random restaurant sales for each day in the configured date range.

    Skips any days defined in sc.DAYS_CLOSED.  
    Iterates over all menu items and creates a sale record for each item per day.

    Returns:
        None
    """
    # fetch menu items from DB
    menu_items = MenuItem.objects

    current_date = sc.START_DATE

    # loop through each day in the date range
    while(current_date <= sc.END_DATE):
        # skip closed days
        if current_date in sc.DAYS_CLOSED:
            current_date += sc.DELTA
            continue
        
        # list to hold all sales for the current day
        daily_sales = []

        # create a sale record for each menu item
        for item in menu_items:
            sale = make_restaurant_sale(current_date, item)
            if sale:
                daily_sales.append(sale)

        # save all sales for the day to the DB
        for sale in daily_sales:
            sale.save()
        
        # move to the next day
        current_date += sc.DELTA

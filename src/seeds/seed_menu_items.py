# adds menu items to the database

from dotenv import load_dotenv
from src.services.db_service import init_db
from src.models.menu_item import MenuItem

# load environment variables for init_db()
load_dotenv(".env.seed")

def seed_menu_items() -> int:
    """
    Define food and beverage menu items and insert them into the MenuItem collection.
    Duplicates are avoided using upsert.

    Returns:
        int: Number of items inserted or updated.
    """
    
    items = [
        {"name": "Buffalo Wings", "category": "Food", "price": 13, "cost": 5.50},
        {"name": "Loaded Nachos", "category": "Food", "price": 12, "cost": 3.00},
        {"name": "Quesadilla", "category": "Food", "price": 12, "cost": 3.25},
        {"name": "Chicken Tenders", "category": "Food", "price": 11, "cost": 3.85},
        {"name": "French Fries", "category": "Food", "price": 4, "cost": 1.40},
        {"name": "Tater Tots", "category": "Food", "price": 4, "cost": 1.75},
        {"name": "Pecan Bleu Salad", "category": "Food", "price": 14, "cost": 5.25},
        {"name": "BLT Salad", "category": "Food", "price": 15, "cost": 5.30},
        {"name": "Taco Salad", "category": "Food", "price": 14, "cost": 3.50},
        {"name": "Pub Burger", "category": "Food", "price": 15, "cost": 5.40},
        {"name": "Patty Melt", "category": "Food", "price": 14, "cost": 4.65},
        {"name": "Fajita Burger", "category": "Food", "price": 15, "cost": 4.95},
        {"name": "Chicken Sandwich", "category": "Food", "price": 13, "cost": 4.40},
        {"name": "Chicken Panini", "category": "Food", "price": 13, "cost": 4.25},
        {"name": "Steak Sandwich", "category": "Food", "price": 15, "cost": 5.35},
        {"name": "Chicken Caesar Wrap", "category": "Food", "price": 13, "cost": 4.15},
        {"name": "BBQ Ribs", "category": "Food", "price": 16, "cost": 5.92},
        {"name": "Pasta Primavera", "category": "Food", "price": 13, "cost": 3.12},
        {"name": "Cajun Roasted Chicken", "category": "Food", "price": 14, "cost": 3.76},
        {"name": "Blackened Salmon", "category": "Food", "price": 17, "cost": 5.25},
        {"name": "Coke", "category": "Beverage", "price": 3, "cost": 0.50},
        {"name": "Diet Coke", "category": "Beverage", "price": 3, "cost": 0.50},
        {"name": "Sprite", "category": "Beverage", "price": 3, "cost": 0.50},
        {"name": "Iced Tea", "category": "Beverage", "price": 3, "cost": 0.40},
        {"name": "Hot Tea", "category": "Beverage", "price": 2.50, "cost": 0.40},
        {"name": "Coffee", "category": "Beverage", "price": 3, "cost": 0.55},
        {"name": "Bottled Water", "category": "Beverage", "price": 2, "cost": 0.15},
        {"name": "Domestic Beer", "category": "Beverage", "price": 6, "cost": 2.00},
        {"name": "Import Beer", "category": "Beverage", "price": 7, "cost": 2.50},
        {"name": "House Red Wine", "category": "Beverage", "price": 8, "cost": 3.00},
    ]
    
    num_items_processed = 0

    for item in items:
        MenuItem.objects(name=item["name"]).update_one(
            upsert=True,
            category=item["category"],
            price=item["price"],
            cost=item["cost"]
        )
        num_items_processed += 1
    
    return num_items_processed


if __name__ == "__main__":
    if init_db():
        result = seed_menu_items()
        print(f"{result} Menu Items seeded.")
    else:
        print("DB connection failed.")
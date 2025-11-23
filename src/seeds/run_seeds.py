# runs all files to seed the database

from dotenv import load_dotenv
from src.services.db_service import init_db
from src.seeds.seed_budget import seed_budget
from src.seeds.seed_events import seed_events
from src.seeds.seed_menu_items import seed_menu_items
from src.seeds.seed_restaurant_sales import seed_restaurant_sales
from src.models import MenuItem, RestaurantSale, Event, Budget

# load environment variables for init_db()
load_dotenv(".env.seed")

def run_seeds() -> None:
    """
    Run all seed scripts to populate the database with initial data.
    
    """
    # seed menu items
    print("Seeding menu items...")
    seed_menu_items()
    print(f"MenuItem collection now has {MenuItem.objects.count()} documents.")
    print("-" * 40)
    
    # seed restaurant sales
    print("Seeding restaurant sales...")
    RestaurantSale.drop_collection()
    seed_restaurant_sales()
    print(f"RestaurantSale collection now has {RestaurantSale.objects.count()} documents.")
    print("-" * 40)

    # seed events
    print("Seeding events...")
    Event.drop_collection()
    seed_events()
    print(f"Event collection now has {Event.objects.count()} documents.")
    print("-" * 40)

    # seed budget
    print("Seeding budgets...")
    Budget.drop_collection()
    seed_budget()
    print(f"Budget collection now has {Budget.objects.count()} documents.")
    print("-" * 40)


if __name__ == "__main__":
    if init_db():
        run_seeds()
        print(f"Seeding complete")
    else:
        print("DB connection failed.")
# adds random events to the database

from datetime import date
import random
from faker import Faker
from src.models.event import Event
from src.utils.constants import EVENT_TYPES 
from src.seeds import seed_constants as sc

# initialize faker for generating fake names
fake = Faker()

def make_event(event_date: date) -> Event:
    """
    Create a single Event for a given date with random client, type, sales, and costs.

    Args:
        event_date (date): The date for which the event should be generated.

    Returns:
        Event: A MongoEngine Event document with randomized fields.
    """
    client_name = f"{fake.first_name()} {fake.last_name()}"
    event_type = random.choice(EVENT_TYPES)
    food_sales = random.randint(sc.MIN_FOOD_SALES, sc.MAX_FOOD_SALES)
    bev_sales = random.randint(sc.MIN_BEV_SALES, sc.MAX_BEV_SALES)
    food_cost = round(food_sales * random.uniform(sc.MIN_FOOD_COST_PCT, sc.MAX_FOOD_COST_PCT), 2)
    bev_cost = round(bev_sales * random.uniform(sc.MIN_BEV_COST_PCT, sc.MAX_BEV_COST_PCT), 2)

    event = Event(
        client_name=client_name,
        event_date=event_date,
        event_type=event_type,
        food_sales=food_sales,
        bev_sales=bev_sales,
        food_cost=food_cost,
        bev_cost=bev_cost
    )

    return event


def seed_events() -> None:
    """
    Seed the database with random events for each day in the configured date range.

    Skips any days defined in sc.DAYS_CLOSED.  
    Generates a random number of events per day and saves each event to the database.

    Returns:
        None
    """
    current_date = sc.START_DATE

    # loop through each day in the date range
    while(current_date <= sc.END_DATE):
        # skip closed days
        if current_date in sc.DAYS_CLOSED:
            current_date += sc.DELTA
            continue

        # generate random number of events for each day
        random_num_events = random.randint(sc.MIN_EVENTS_PER_DAY, sc.MAX_EVENTS_PER_DAY)

        # create and save each event
        for i in range(random_num_events):
            event = make_event(current_date)
            event.save()
        
        # move to the next day
        current_date += sc.DELTA

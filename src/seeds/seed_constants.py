# constants used for seeding scripts
from datetime import date, timedelta

# date constants
START_DATE = date(2024, 1, 1)
END_DATE = date(2025, 12, 31)
DELTA = timedelta(days=1)
DAYS_CLOSED = {
    # christmas
    date(2024, 12, 25), 
    date(2025, 12, 25),
    # thanksgiving
    date(2024, 11, 28),
    date(2025, 11, 27),
    # bad weather
    date(2024, 2, 2),
    date(2025, 1, 17)
}

# event detail constants
MIN_EVENTS_PER_DAY = 0
MAX_EVENTS_PER_DAY = 3
MIN_FOOD_SALES = 750
MAX_FOOD_SALES = 3100
MIN_BEV_SALES = 200
MAX_BEV_SALES = 1500
MIN_FOOD_COST_PCT = 0.28
MAX_FOOD_COST_PCT = 0.41
MIN_BEV_COST_PCT = 0.15
MAX_BEV_COST_PCT = 0.25

# restaurant sale constants
MIN_QTY_SOLD = 0
MAX_FOOD_QTY_SOLD = 15
MAX_BEV_QTY_SOLD = 25 

# budget constants
MIN_SALES_VARIANCE = 0.9
MAX_SALES_VARIANCE = 1.1
MIN_COST_VARIANCE = 0.97
MAX_COST_VARIANCE = 1.03
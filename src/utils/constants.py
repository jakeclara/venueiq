# shared constants used across the app

# month options for dropdown filters
MONTHS = [
    {"label": month_name, "value": month_number}
    # enumerate to map month numbers to month names
    for month_number, month_name in enumerate([
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ], start=1)
]

# year options for dropdown filters (only one option for demo)
YEARS = [{"label": "2025", "value": 2025}]


# event types for banquet event model
EVENT_TYPES = [
    "Wedding", 
    "Corporate",
    "Birthday Party",
    "Anniversary",
    "Holiday Party",
    "Other"
]

# menu item types for menu item model
MENU_CATEGORIES = ["Food", "Beverage"]
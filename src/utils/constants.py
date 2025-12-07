# shared constants used across the app

# color theme for the app (Bootstrap FLATLY theme)
THEME_COLORS = {
    "primary": "#2c3e50",
    "secondary": "#95a5a6",
    "success": "#18bc9c",
    "danger": "#e74c3c",
    "warning": "#f39c12",
    "info": "#3498db",
    "light": "#ecf0f1",
    "dark": "#7b8a8b",
}

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
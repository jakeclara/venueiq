# Month options
# Use enumerate to map month numbers to month names
MONTHS = [
    {"label": month_name, "value": month_number}
    for month_number, month_name in enumerate([
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ], start=1)
]

# Year options (only one option for demo)
YEARS = [{"label": "2025", "value": 2025}]

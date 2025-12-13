# src/callbacks/register_callbacks.py

from src.callbacks.budget_callbacks import get_budget_page_callbacks
from src.callbacks.event_callbacks import get_event_callbacks
from src.callbacks.home_callbacks import get_home_callbacks
from src.callbacks.restaurant.snapshot_callbacks import get_restaurant_snapshot_callbacks
from src.callbacks.restaurant.statement_callbacks import get_restaurant_statement_callbacks


def register_all_callbacks(app):
    """Registers all callbacks for the app."""
    get_home_callbacks(app)
    get_event_callbacks(app)
    get_restaurant_snapshot_callbacks(app)
    get_restaurant_statement_callbacks(app)
    get_budget_page_callbacks(app)
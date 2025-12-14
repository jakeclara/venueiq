# contains callbacks related to the restaurant statement page table
from dash import Input, Output

from src.components.core import statement_builder
from src.metrics.restaurant import statement_metrics
from src.utils.decorators import handle_callback_errors


# fallback outputs for error handling
RESTAURANT_STATEMENT_PAGE_ERROR_FALLBACKS = ([],)

def get_restaurant_statement_callbacks(app):
    @app.callback(
        Output("restaurant-statement-table", "data"),
        Input("month-dropdown", "value"),
        Input("year-dropdown", "value"),
    )
    @handle_callback_errors(fallback_outputs=RESTAURANT_STATEMENT_PAGE_ERROR_FALLBACKS)
    def update_restaurant_statement_page(month, year):

        metrics = statement_metrics.get_statement_metrics(month, year)
        rows = statement_builder.build_statement_rows(metrics)
        
        return rows
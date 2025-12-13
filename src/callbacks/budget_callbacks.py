# contains callbacks related to the budget page table
from dash import Input, Output

from src.components.budget import budget_builder
from src.metrics import budget_metrics

def get_budget_page_callbacks(app):
    @app.callback(
        Output("budget-table", "data"),
        Input("year-dropdown", "value"),
    )
    def update_budget_page(year):
        """Update budget table component based on selected year."""
        
        metrics = budget_metrics.get_annual_budget_data(year)
        rows = budget_builder.build_budget_table_rows(metrics)
        
        return rows
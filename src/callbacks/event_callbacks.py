# contains callbacks related to the event page visualizations

from dash import Input, Output

from src.components import cards, charts, ui_helpers
from src.metrics import event_metrics
from src.utils.constants import THEME_COLORS

def get_event_callbacks(app):
    @app.callback(
        Output("event-monthly-summary-card", "children"),
        Output("event-ytd-bar-chart", "figure"),
        Input("month-dropdown", "value"),
        Input("year-dropdown", "value"),
    )
    def update_event_page(month, year):
        """Update all Event dashboard visual components based on selected month/year."""

        monthly_revenue_metrics = event_metrics.get_events_monthly_revenue_metrics(month, year)
        py_monthly_revenue_metrics = event_metrics.get_events_monthly_revenue_metrics(month, year - 1)

        ytd_revenue_metrics = event_metrics.get_events_ytd_revenue_metrics(month, year)

        event_monthly_summary_card = cards.make_revenue_by_dept_card(
            title="Monthly Summary",
            current=monthly_revenue_metrics,
            prior=py_monthly_revenue_metrics,
            departments=["Food", "Beverage"],
            current_variance_color=ui_helpers.get_variance_color(monthly_revenue_metrics['variance']),
            py_variance_color=ui_helpers.get_variance_color(py_monthly_revenue_metrics['variance'])
        )

        events_ytd_bar_chart_colors = {
            "actual": THEME_COLORS["success"],
            "py": THEME_COLORS["warning"],
            "budgeted": THEME_COLORS["info"]
        }

        events_ytd_bar_chart = charts.make_grouped_revenue_bar_chart(
            ytd_revenue_metrics,
            color_map=events_ytd_bar_chart_colors
        )

        return (
            event_monthly_summary_card,
            events_ytd_bar_chart
        )

        
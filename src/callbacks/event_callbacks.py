# contains callbacks related to the event page visualizations

from dash import Input, Output

from src.components.events import events_page_builders
from src.metrics import event_metrics

def get_event_callbacks(app):
    @app.callback(
        Output("event-monthly-summary-card", "children"),
        Output("event-ytd-bar-chart", "figure"),
        Output("num-events-card", "children"),
        Output("num-high-value-events-card", "children"),
        Output("avg-event-sales-card", "children"),
        Output("top-five-events-card", "children"),
        Output("event-type-pie-chart", "figure"),
        Input("month-dropdown", "value"),
        Input("year-dropdown", "value"),
    )
    def update_event_page(month, year):
        """Update all Event dashboard visual components based on selected month/year."""

        # get all data
        data = event_metrics.get_events_page_data(month, year)

        # build visualizations
        event_monthly_summary_card = events_page_builders.build_events_monthly_summary_card(
            data["monthly_revenue_metrics"],
            data["py_monthly_revenue_metrics"]
        )

        events_ytd_bar_chart = events_page_builders.build_events_ytd_bar_chart(
            data["ytd_summary_metrics"]
        )

        num_events_card = events_page_builders.build_num_events_card(
            data["num_events_monthly"],
            data["num_events_ytd"]
        )

        num_high_value_events_card = events_page_builders.build_num_high_value_events_card(
            data["num_high_value_events_monthly"],
            data["num_high_value_events_ytd"]
        )

        avg_event_sales_card = events_page_builders.build_avg_event_sales_card(
            data["avg_event_sales_monthly"],
            data["avg_event_sales_ytd"]
        )

        top_five_events_monthly_card = events_page_builders.build_top_five_monthly_events_card(
            data["top_five_events_monthly"]
        )

        event_type_pie_chart = events_page_builders.build_event_type_pie_chart(
            data["events_by_type_df"]
        )


        return (
            event_monthly_summary_card,
            events_ytd_bar_chart,
            num_events_card,
            num_high_value_events_card,
            avg_event_sales_card,
            top_five_events_monthly_card,
            event_type_pie_chart
        )

        
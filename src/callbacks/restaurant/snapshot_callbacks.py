# contains callbacks related to the restaurant snapshot page visualizations

from dash import Input, Output

from src.components.restaurant import restaurant_snapshot_builders
from src.metrics.restaurant import restaurant_snapshot_metrics

def get_restaurant_snapshot_callbacks(app):
    @app.callback(
        Output("avg-sales-by-day-line-chart", "figure"),
        Output("top-five-menu-items-card", "children"),
        Output("hot-menu-items-card", "children"),
        Output("cold-menu-items-card", "children"),
        Output("sales-by-category-pie-chart", "figure"),
        Input("month-dropdown", "value"),
        Input("year-dropdown", "value"),
    )
    def update_restaurant_snapshot_page(month, year):
        """Update all Restaurant Snapshot dashboard visual components based on selected month/year."""

        # get all data
        data = restaurant_snapshot_metrics.get_restaurant_snapshot_page_data(month, year)

        # build visualizations
        avg_sales_by_day_line_chart = restaurant_snapshot_builders.build_avg_Sales_by_day_chart(
            data["avg_sales_by_day"]
        )

        top_five_menu_items_card = restaurant_snapshot_builders.build_top_five_menu_items_card(
            data["top_five_menu_items"]
        )

        hot_menu_items_card = restaurant_snapshot_builders.build_hot_menu_items_card(
            data["hot_menu_items"]
        )

        cold_menu_items_card = restaurant_snapshot_builders.build_cold_menu_items_card(
            data["cold_menu_items"]
        )

        sales_by_category_pie_chart = restaurant_snapshot_builders.build_sales_by_category_pie_chart(
            data["sales_by_category"]
        )


        return (
            avg_sales_by_day_line_chart,
            top_five_menu_items_card,
            hot_menu_items_card,
            cold_menu_items_card,
            sales_by_category_pie_chart,
        )
# contains callbacks related to the home page visualizations

from dash import Input, Output
import pandas as pd

from src.components import cards, charts, ui_helpers
from src.utils.constants import THEME_COLORS
from src.metrics import home_metrics

def get_home_callbacks(app):
    @app.callback(
        Output("monthly-revenue-progress-chart", "figure"),
        Output("monthly-summary-card", "children"),
        Output("ytd-revenue-card", "children"),
        Output("cogs-kpi-card", "children"),
        Output("profit-card", "children"),
        Output("top-menu-item-card", "children"),
        Output("top-event-card", "children"),
        Output("revenue-breakdown-pie-chart", "figure"),
        Input("month-dropdown", "value"),
        Input("year-dropdown", "value"),
    )
    def update_home_page(month, year):
        """Update all Home dashboard visual components based on selected month/year."""

        monthly_revenue_metrics = home_metrics.get_combined_monthly_revenue_metrics(month, year)
        py_monthly_revenue_metrics = home_metrics.get_combined_monthly_revenue_metrics(month, year - 1)
        ytd_revenue_metrics = home_metrics.get_combined_ytd_revenue_metrics(month, year)
        py_ytd_revenue_metrics = home_metrics.get_combined_ytd_revenue_metrics(month, year - 1)
        
        ytd_cost_metrics = home_metrics.get_combined_ytd_cost_metrics(month, year)
        ytd_gross_profit = home_metrics.compute_gross_profit(
            ytd_revenue_metrics['total_revenue'],
            ytd_cost_metrics['actual_total_costs'],
            ytd_revenue_metrics['budgeted_revenue'],
            ytd_cost_metrics['budgeted_total_costs']
        )

        cogs_pct_metrics = home_metrics.compute_cogs_pct_metrics(ytd_revenue_metrics, ytd_cost_metrics)

        top_menu_item = home_metrics.get_top_menu_item(period="ytd", month=month, year=year)
        py_top_menu_item = home_metrics.get_top_menu_item(period="ytd", month=month, year=year - 1)

        top_selling_event = home_metrics.get_top_event(period="ytd", month=month, year=year)
        py_top_selling_event = home_metrics.get_top_event(period="ytd", month=month, year=year - 1)

        donut_colors = ui_helpers.get_donut_chart_colors(
            monthly_revenue_metrics['total_revenue'],
            monthly_revenue_metrics['budgeted_revenue']
        )

        donut_chart = charts.make_budget_donut(
            actual=monthly_revenue_metrics['total_revenue'],
            budgeted=monthly_revenue_metrics['budgeted_revenue'],
            color_map=donut_colors
        )
        
        monthly_summary_card = cards.make_revenue_by_dept_card(
            title="Monthly Summary",
            current=monthly_revenue_metrics,
            prior=py_monthly_revenue_metrics,
            departments=["Restaurant", "Events"],
            current_variance_color=ui_helpers.get_variance_color(monthly_revenue_metrics['variance']),
            py_variance_color=ui_helpers.get_variance_color(py_monthly_revenue_metrics['variance'])
        )

        ytd_revenue_card_metrics = [
            {
                "name": "Actual",
                "value": ytd_revenue_metrics['total_revenue'],
                "budget": ytd_revenue_metrics['budgeted_revenue'],
                "variance": ytd_revenue_metrics['variance'],
            },
            {
                "name": "Prior Year",
                "value": py_ytd_revenue_metrics['total_revenue'],
                "budget": py_ytd_revenue_metrics['budgeted_revenue'],
                "variance": py_ytd_revenue_metrics['variance'],
            },
        ]

        ytd_revenue_card = cards.make_two_metrics_card(
            title="YTD Revenue",
            metrics=ytd_revenue_card_metrics,
            footer="vs. Budget",
            symbol="$"
        )

        cogs_kpi_card_metrics = [
            {
                "name": "Restaurant",
                "value": cogs_pct_metrics['restaurant_actual_cogs_pct'],
                "budget": cogs_pct_metrics['restaurant_budgeted_cogs_pct'],
                "variance": cogs_pct_metrics['restaurant_actual_cogs_pct'] - cogs_pct_metrics['restaurant_budgeted_cogs_pct'],
            },
            {
                "name": "Events",
                "value": cogs_pct_metrics['event_actual_cogs_pct'],
                "budget": cogs_pct_metrics['event_budgeted_cogs_pct'],
                "variance": cogs_pct_metrics['event_actual_cogs_pct'] - cogs_pct_metrics['event_budgeted_cogs_pct'],
            },
        ]

        cogs_kpi_card = cards.make_two_metrics_card(
            title="YTD Cost of Goods Sold",
            metrics=cogs_kpi_card_metrics,
            footer="vs. Budget",
            symbol="%",
        )

        profit_card_metrics = [
            {
                "name": "Actual",
                "value": ytd_gross_profit['actual'],
                "budget": ytd_gross_profit['budgeted'],
                "variance": ytd_gross_profit['actual'] - ytd_gross_profit['budgeted'],
            },
        ]

        profit_card = cards.make_one_metric_card(
            title="YTD Gross Profit",
            metric=profit_card_metrics[0],
            footer="vs. Budget",
            symbol="$",
        )

        top_menu_item_metrics = {
                "name": top_menu_item["name"],
                "value": top_menu_item["total_sales"],
                "variance": top_menu_item["total_sales"] - py_top_menu_item["total_sales"],
        }

        top_menu_item_card = cards.make_one_metric_card(
            title="Top Selling Menu Item",
            metric=top_menu_item_metrics,
            footer="YTD vs. Same Item Sales Prior Year",
            symbol="$",
        )

        top_event_card_metrics = {
                "name": top_selling_event["name"],
                "value": top_selling_event["total_sales"],
                "variance": top_selling_event["total_sales"] - py_top_selling_event["total_sales"],
        }

        top_event_card = cards.make_one_metric_card(
            title="Top Selling Event",
            metric=top_event_card_metrics,
            footer="vs. Top Selling Event Prior Year",
            symbol="$",
        )

        revenue_breakdown_df = pd.DataFrame([
            {
                "name": "Restaurant",
                "value": ytd_revenue_metrics['restaurant_revenue'],
                "color": THEME_COLORS["success"]
            },
            {
                "name": "Events",
                "value": ytd_revenue_metrics['event_revenue'],
                "color": THEME_COLORS["warning"]
            }
        ])

        revenue_breakdown_pie = charts.make_pie_chart(
            data=revenue_breakdown_df,
            names="name",
            values="value",
            color="color"
        )

        return (
            donut_chart,
            monthly_summary_card,
            ytd_revenue_card,
            cogs_kpi_card,
            profit_card,
            top_menu_item_card,
            top_event_card,
            revenue_breakdown_pie,
        )

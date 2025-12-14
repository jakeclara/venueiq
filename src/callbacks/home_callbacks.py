# contains callbacks related to the home page visualizations

from dash import Input, Output

from src.components.core.ui_helpers import make_error_card
from src.components.home import home_page_builders
from src.metrics.home import home_metrics
from src.utils.decorators import handle_callback_errors

# fallback outputs for error handling
HOME_PAGE_ERROR_FALLBACKS = (
    {},
    make_error_card(),
    make_error_card(),
    make_error_card(),
    make_error_card(),
    make_error_card(),
    make_error_card(),
    {},
)

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
    @handle_callback_errors(fallback_outputs=HOME_PAGE_ERROR_FALLBACKS)
    def update_home_page(month, year):
        """Update all Home dashboard visual components based on selected month/year."""
    
        # get all data
        data = home_metrics.get_home_page_data(month, year)

        # build visualizations
        donut_chart = home_page_builders.build_donut_chart(
            data['monthly_revenue_metrics']
        )

        monthly_summary_card = home_page_builders.build_monthly_summary_card(
            data['monthly_revenue_metrics'],
            data['py_monthly_revenue_metrics']
        )

        ytd_revenue_card = home_page_builders.build_ytd_revenue_card(
            data['ytd_revenue_metrics'],
            data['py_ytd_revenue_metrics']
        )
        
        cogs_kpi_card = home_page_builders.build_cogs_kpi_card(
            data['cogs_pct_metrics']
        )

        profit_card = home_page_builders.build_profit_card(
            data['ytd_gross_profit'],
            data['budgeted_ytd_gross_profit']
        )
        
        top_menu_item_card = home_page_builders.build_top_menu_item_card(
            data['top_menu_item'],
            data['py_top_menu_item']
        )

        top_event_card = home_page_builders.build_top_event_card(
            data['top_selling_event'],
            data['py_top_selling_event']
        )

        revenue_breakdown_pie_chart = home_page_builders.build_revenue_breakdown_pie_chart(
            data['ytd_revenue_metrics']
        )


        return (
            donut_chart,
            monthly_summary_card,
            ytd_revenue_card,
            cogs_kpi_card,
            profit_card,
            top_menu_item_card,
            top_event_card,
            revenue_breakdown_pie_chart,
        )

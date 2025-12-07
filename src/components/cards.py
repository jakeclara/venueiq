# contains reusable card components for the dashoboard

from dash import dcc, html
import dash_bootstrap_components as dbc

from src.components.ui_helpers import variance_bar
from src.metrics.metrics_helpers import format_metric



def make_chart_card(title: str, chart: dcc.Graph) -> dbc.Card:
    """
    Returns a dbc.Card object with the title and chart.
    
    Args:
        title (str): The title of the card.
        chart (dcc.Graph): The chart to display in the card.
    
    Returns:
        dbc.Card: A dbc.Card object with the title and chart.
    """
    return dbc.Card([
        dbc.CardHeader(html.H5(title, className="card-title")),
        dbc.CardBody(chart)
    ], className="dashboard-card"
)


def make_one_metric_card(title: str, metric: dict, footer: str, symbol: str="$") -> dbc.Card:
    """
    Returns a dbc.Card object with the title, metric value, and footer.
    
    Args:
        title (str): The title of the card.
        metric (dict): A dictionary containing the metric name and value.
        footer (str): The footer of the card.
        symbol (str): The symbol to display with the metric value. Defaults to "$".
    
    Returns:
        dbc.Card: A dbc.Card object with the title, metric value, and footer.
    """
    return dbc.Card([
        dbc.CardHeader(html.H5(title, className="card-title")),
        dbc.CardBody([
            html.P(metric["name"], className="text-muted mb-1 text-center"),
            html.H4(
                # format the metric value with the given symbol
                format_metric(metric["value"], symbol),
                className="mb-3 text-center",
            ),
            html.Div(variance_bar(metric.get("variance", 0))),
            html.Small(
                format_metric(metric.get('variance', 0), symbol),
                className="d-block text-center text-muted mt-1"
            ),
        ]),
        dbc.CardFooter(html.Small(footer, className="text-muted d-block")),
    ], className="dashboard-card kpi-card"
)


def make_two_metrics_card(title: str, metrics: list[dict], footer: str, symbol: str="$") -> dbc.Card:
    """
    Returns a dbc.Card object with the title, two metrics, and footer.
    
    Args:
        title (str): The title of the card.
        metrics (list[dict]): A list of dictionaries containing the metric name and value.
        footer (str): The footer of the card.
        symbol (str): The symbol to display with the metric values. Defaults to "$".
    
    Returns:
        dbc.Card: A dbc.Card object with the title, two metrics, and footer.
    """
    return dbc.Card([
        dbc.CardHeader(html.H5(title, className="card-title")),
        dbc.CardBody(
            dbc.Row([
                dbc.Col([
                    html.P(metric["name"], className="text-muted mb-1 text-center"),
                    html.H4(
                        format_metric(metric["value"], symbol),
                        className="mb-3 text-center",
                    ),
                    html.Div(variance_bar(metric.get("variance", 0))),
                    html.Small(
                        format_metric(metric.get('variance', 0), symbol),
                        className="d-block text-center text-muted mt-1"
                    ),
                ], width=6)
                # loop through the metrics list and create a dbc.Col for each metric
                for metric in metrics
            ])
        ),
        dbc.CardFooter(html.Small(footer, className="text-muted d-block")),
    ], className="dashboard-card kpi-card"
)


def make_revenue_by_dept_card(
        title: str,
        current: dict,
        prior: dict,
        departments: list[str],
        current_variance_color: str = "black",
        py_variance_color: str = "black"
) -> dbc.Card:
    """
    Returns a dbc.Card object with the title and a table of current and prior year revenue by department.
    
    Args:
        title (str): The title of the card.
        current (dict): A dictionary containing the current year revenue by department.
        prior (dict): A dictionary containing the prior year revenue by department.
        departments (list[str]): A list of department names.
        current_variance_color (str): The color to use for the current year variance. Defaults to "black".
        py_variance_color (str): The color to use for the prior year variance. Defaults to "black".
    
    Returns:
        dbc.Card: A dbc.Card object with the title and a table of current and prior year revenue by department.
    """
    card = dbc.Card([
        dbc.CardHeader(html.H5(title, className="card-title"),
        ),
        dbc.CardBody([
            dbc.Row([
                dbc.Col(html.P("Department")),
                dbc.Col(html.P("Current")),
                dbc.Col(html.P("Prior Year")),
            ],
            className="fw-bold mb-1"),
            dbc.Row([
                dbc.Col(html.P(departments[0])), 
                dbc.Col(html.P(f"${current[f'{departments[0].lower()}_revenue']:,.0f}")),
                dbc.Col(html.P(f"${prior[f'{departments[0].lower()}_revenue']:,.0f}")),
            ],
            className="mb-1"),
            dbc.Row([
                dbc.Col(html.P(departments[1])),
                dbc.Col(html.P(f"${current[f'{departments[1].lower()}_revenue']:,.0f}")),
                dbc.Col(html.P(f"${prior[f'{departments[1].lower()}_revenue']:,.0f}"))
            ],
            className="mb-1"),
            dbc.Row([
                dbc.Col(html.P("Total Revenue")),
                dbc.Col(html.P(f"${current['total_revenue']:,.0f}")),
                dbc.Col(html.P(f"${prior['total_revenue']:,.0f}"))
            ],
            className="mb-1"),
            dbc.Row([
                dbc.Col(html.P("Total Budgeted Revenue")),
                dbc.Col(html.P(f"${current['budgeted_revenue']:,.0f}")),
                dbc.Col(html.P(f"${prior['budgeted_revenue']:,.0f}"))
            ],
            className="mb-1"),
            dbc.Row([
                dbc.Col(html.P("Variance")),
                dbc.Col(html.P(f"${current['variance']:,.0f}", style={"color": current_variance_color})),
                dbc.Col(html.P(f"${prior['variance']:,.0f}", style={"color": py_variance_color}))
            ])
        ])
    ], className="dashboard-card")
    
    return card

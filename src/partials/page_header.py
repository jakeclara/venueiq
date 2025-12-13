# shared page header component for pages

from typing import Optional
from dash.development.base_component import Component
import dash_bootstrap_components as dbc

from src.partials import make_title_bar


def make_page_header(page_name: str, filter_component: Optional[Component] = None) -> Component:
    """
    Returns a dbc.Row object with a title bar and a filter component.
    
    Args:
        page_name (str): The name of the page.
        filter_component (Optional[Component], optional): The filter component to display in the page header. Defaults to None.
    
    Returns:
        Component: A dbc.Row object with a title bar and a filter component.
    """
    return dbc.Row([
        dbc.Col([
            make_title_bar(page_name),
            ], xs=12, lg=6, className="mb-4"
        ),
        dbc.Col([
            filter_component if filter_component else []
        ], xs=12, lg=6, className="mb-4"),
    ], className="align-items-center"
    )
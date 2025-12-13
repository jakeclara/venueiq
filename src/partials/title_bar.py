# shared title bar component for pages

import dash
from dash import html
import dash_bootstrap_components as dbc
from dash.development.base_component import Component


def make_title_bar(page_module: str) -> Component:
    """
    Returns a dbc.Row object with a title bar containing the name and description of a page.

    Args:
        page_module (str): The name of the page module.

    Returns:
        Component: A dbc.Row object with a title bar containing the name and description of a page.
    """
    meta_data = dash.page_registry[page_module]

    title_bar = dbc.Row([
        dbc.Col([
            html.H3(meta_data['name']),
            html.Hr(),
            html.Small(meta_data['description'], className="text-muted")
        ])
    ])

    return title_bar
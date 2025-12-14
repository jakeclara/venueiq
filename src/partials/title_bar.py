# shared title bar component for pages

import dash
from dash import html
import dash_bootstrap_components as dbc
from dash.development.base_component import Component
import logging

# create logger
logger = logging.getLogger(__name__)


def make_title_bar(page_module: str) -> Component:
    """
    Returns a dbc.Row object with a title bar containing the name and description of a page.
    
    Args:
        page_module (str): The name of the page module.
    
    Returns:
        Component: A dbc.Row object with a title bar containing the name and description of a page.
    """
    try:
        # get the meta data for the page module
        meta_data = dash.page_registry[page_module]

        # create the title bar
        title_bar = dbc.Row([
            dbc.Col([
                html.H3(meta_data['name']),
                html.Hr(),
                html.Small(meta_data['description'], className="text-muted")
            ])
        ])

        return title_bar
    
    except KeyError as e:
        # log error if page module not found
        logger.error(f"Page module {page_module} not found in page registry.")
        logger.exception(e)
        # return a warning message
        return dbc.Row(dbc.Col(html.Div("Error: Page metadata missing.", className="text-danger")))
    
    except Exception as e:
        # log error if any other exception occurs
        logger.error(f"Error in make_title_bar for: {page_module}.")
        return dbc.Row(dbc.Col(html.Div()))

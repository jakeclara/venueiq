# shared footer component for pages

from dash import html
import dash_bootstrap_components as dbc

# footer layout
footer = html.Footer(
    dbc.Container(
        [
            html.Div(
                "© 2025 VenueIQ",
                className="footer-text"
            )
        ]
    ),
    className="bg-primary mt-auto py-3"
)
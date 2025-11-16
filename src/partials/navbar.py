# shared navbar component for pages
# adapted from: https://www.dash-bootstrap-components.com/docs/components/navbar/

import dash_bootstrap_components as dbc
from dash import Input, Output, State, callback, html

# main navbar component
navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # logo and brand, vertically centered
                dbc.Row(
                    [
                        dbc.Col(html.I(className="bi bi-graph-up custom-navbar-icon")),
                        dbc.Col(dbc.NavbarBrand("VenueIQ", className="custom-navbar-brand ms-2")),
                    ],
                    align="center",
                    className="g-0",
                ),
                href="/",
                className="custom-navbar-link"
            ),
            # navbar toggler for small screens
            dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
            # collapsible nav items
            dbc.Collapse(
                dbc.Nav (
                    [
                        dbc.NavItem(
                            dbc.NavLink(
                                "Home",
                                href='/'
                            )
                        ),
                        dbc.DropdownMenu(
                            children=[
                                dbc.DropdownMenuItem("Snapshot", href="/restaurant/snapshot"),
                                dbc.DropdownMenuItem("Statement", href="/restaurant/statement"),
                            ],
                            nav=True,
                            in_navbar=True,
                            label="Restaurant",
                        ),
                        dbc.NavItem(
                            dbc.NavLink(
                                "Banquet",
                                href='/banquet'
                            )
                        ),
                        dbc.NavItem(
                            dbc.NavLink(
                                "Budget",
                                href='/budget'
                            )
                        ),
                    ]
                ),
                id="navbar-collapse",
                is_open=False,
                navbar=True,
            ),
        ]
    ),
    color="primary",
    dark=True,
)


# add callback for toggling the collapse on small screens
@callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open
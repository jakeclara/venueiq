import dash
import dash_bootstrap_components as dbc
from dash import Dash, html
from flask import Flask
from partials import navbar, footer

# explicit Flask server
server = Flask(__name__)

# initialize the app
app = Dash(
    __name__,
    server=server,
    # use Dash pages
    use_pages=True,
    # use BS Flatly theme and icons
    external_stylesheets=[dbc.themes.FLATLY, dbc.icons.BOOTSTRAP]
)

# define layout 
def serve_layout():
    return html.Div(
        [
            navbar,
            dbc.Container(dash.page_container),
            footer
        ],
        className="d-flex flex-column min-vh-100"
    )

# set layout with serve_layout function
app.layout = serve_layout

# set server for deployment
server = app.server

# run the app
if __name__ == '__main__':
    app.run(debug=True)
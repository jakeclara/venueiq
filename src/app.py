import dash
import dash_bootstrap_components as dbc
from dash import Dash, html
from flask import Flask

from src.partials import navbar, footer, month_year_filters
from src.services.db_service import init_db
from dotenv import load_dotenv
from src.callbacks.home_callbacks import get_home_callbacks
from src.callbacks.event_callbacks import get_event_callbacks

# load environment variables from .env file
load_dotenv()

# initialize the database
if not init_db():
    print("Database initialization failed.")

# explicit Flask server
server = Flask(__name__)

# initialize the app
app = Dash(
    __name__,
    server=server,
    # use Dash pages
    use_pages=True,
    # use BS Flatly theme and icons
    external_stylesheets=[dbc.themes.FLATLY, dbc.icons.BOOTSTRAP],
    # suppress callback exceptions
    suppress_callback_exceptions=True
)

# define layout 
def serve_layout():
    return html.Div(
        [
            navbar,
            dbc.Container(month_year_filters, className="mt-4"),
            dbc.Container(dash.page_container, className="mt-4"),
            footer
        ],
        className="d-flex flex-column min-vh-100"
    )

# set layout with serve_layout function
app.layout = serve_layout

# get callbacks for each page
get_home_callbacks(app)
get_event_callbacks(app)

# set server for deployment
server = app.server

# run the app
if __name__ == '__main__':
    app.run(debug=True)
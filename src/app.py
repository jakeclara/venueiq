import dash
import dash_bootstrap_components as dbc
from dash import Dash, dcc, html
from dotenv import load_dotenv
import logging

from src.callbacks.register_callbacks import register_all_callbacks
from src.partials import navbar, footer
from src.services.db_service import init_db
from src.utils.log_config import setup_logging

# create logger
logger = logging.getLogger(__name__)

# set up logging
setup_logging()

# load environment variables from .env file
load_dotenv()

# initialize the database
try:
    init_db()
except Exception as e:
    logger.critical(f"Database initialization failed: Program must exit")
    raise

# initialize the app
app = Dash(
    __name__,
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
            dcc.Loading(
                type="default",
                children=dbc.Container(dash.page_container, className="mt-4"),
            ),
            footer
        ],
        className="d-flex flex-column min-vh-100"
    )

# set layout with serve_layout function
app.layout = serve_layout

# register all callbacks
register_all_callbacks(app)

# set server for deployment
server = app.server

# run the app
if __name__ == '__main__':
    app.run(debug=False)
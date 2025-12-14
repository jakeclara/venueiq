# configure logging for the app
# reference: https://docs.python.org/3/howto/logging.html

import logging
import sys

def setup_logging():
    """
    Configure logging for the app.

    This function sets up logging to the standard output with a logging
    level of INFO and a format of '%(asctime)s - %(name)s - %(levelname)s - %(message)s'.
    """
    logging.basicConfig(
        stream=sys.stdout,
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
)

    logging.getLogger('werkzeug').setLevel(logging.WARNING)
    logging.getLogger('dash').setLevel(logging.WARNING)
    logging.info("Logging initialized")
# service to connect to the database

from mongoengine import connect
import os
import logging

# create logger
logger = logging.getLogger(__name__)

def validate_env_vars(*variables: str) -> bool:
    """
    Validate that all specified environment variables exist.

    Args:
        *variables (str): One or more environment variable names to check.

    Returns:
        bool: True if all variables exist, False if any are missing.
    """
    for var in variables:
        if not os.getenv(var):
            return False
    return True


def init_db() -> None:    
    """
    Initializes the database connection.

    :raises EnvironmentError: If any of the required environment variables are missing.
    :raises Exception: If the database connection fails.
    """
    if not validate_env_vars("MONGO_USER", "MONGO_PASSWORD", "MONGO_HOST", "MONGO_DB"):
        logger.critical("Environment variable missing")
        raise EnvironmentError("Cannot connect to DB: Environment variable missing")
    
    user = os.getenv("MONGO_USER")
    password = os.getenv("MONGO_PASSWORD")
    host = os.getenv("MONGO_HOST")
    db = os.getenv("MONGO_DB")
    uri = f"mongodb+srv://{user}:{password}@{host}/{db}?retryWrites=true&w=majority"

    logger.info(f"Trying to connect to DB at {host}/{db}")

    try:
        connect(host=uri)
        logger.info("DB connection successful...")
    except Exception as e:
        logger.error(f"DB connection failed")
        raise Exception(f"DB connection failed : {e}") from e
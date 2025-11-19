# service to connect to the database

from mongoengine import connect
import os

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


def init_db() -> bool:
    """
    Connect to the MongoDB database using environment variables.

    Assumes that the required environment variables have already 
    been loaded.

    Returns:
        bool: True if the connection was successful, False otherwise.
    """      

    if not validate_env_vars("MONGO_USER", "MONGO_PASSWORD", "MONGO_HOST", "MONGO_DB"):
        # TODO: remove this debug print statement
        print("Environment variable missing")
        return False
    
    user = os.getenv("MONGO_USER")
    password = os.getenv("MONGO_PASSWORD")
    host = os.getenv("MONGO_HOST")
    db = os.getenv("MONGO_DB")
    uri = f"mongodb+srv://{user}:{password}@{host}/{db}?retryWrites=true&w=majority"

    try:
        connect(host=uri)
        # TODO: remove this debug print statement
        print("Connection successful...")
        return True
    except Exception as e:
        # TODO: remove this debug print statement
        print(f"Connection failed: {e}")
        return False
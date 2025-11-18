# service to connect to the database

from mongoengine import connect
import os
from dotenv import load_dotenv

def validate_env_vars(*variables):
    ''' validates that environment variables exist '''
    for var in variables:
        # if variable does not exist
        if not os.getenv(var):
                # return false
                return False
    
    # return true only if all variables exist
    return True


# load environment variables
load_dotenv()

def init_db():
    ''' connects to database '''      

    # if environment variables are NOT available
    if not validate_env_vars("MONGO_USER", "MONGO_PASSWORD", "MONGO_HOST", "MONGO_DB"):
        # TODO: remove this debug print statement
        print("Environment variable missing")
        # false indicates unsuccessful connection
        return False
    
    # get user and pass
    user = os.getenv("MONGO_USER")
    password = os.getenv("MONGO_PASSWORD")

    # get connection variables
    host = os.getenv("MONGO_HOST")
    db = os.getenv("MONGO_DB")

    # build connection string
    uri = f"mongodb+srv://{user}:{password}@{host}/{db}?retryWrites=true&w=majority"

    # try to connect to db
    try:
        # use MongoEngine connect method
        connect(host=uri)
        # TODO: remove this debug print statement
        print("Connection successful...")
        # true indicates successful connection
        return True
    except Exception as e:
        # TODO: remove this debug print statement
        print(f"Connection failed: {e}")
        # false indicates unsuccessful connection
        return False
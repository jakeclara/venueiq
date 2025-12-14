# contains decorators to handle exceptions

# adapted from: https://community.plotly.com/t/error-handling-for-callbacks-and-layouts/83586

import logging
from functools import wraps
from typing import Any, Callable, Optional, Tuple

logger = logging.getLogger(__name__)

def safe_query(fallback: Optional[Any] = None) -> Callable:
    """
    A decorator to catch and log exceptions.

    If an exception occurs, it logs the error and
    returns the fallback value if provided.

    Args:
        fallback (Any, optional): The value to return if an exception occurs.

    Returns:
        Callable: A decorator that catches and logs exceptions in a callback.
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                # execute the original function
                return func(*args, **kwargs)
            # catch and log exceptions
            except Exception as e:
                logger.error(
                    f"Error in {func.__name__}: {e}",
                    exc_info=True,
                )
                # return the fallback value
                return fallback
        return wrapper
    return decorator


def handle_callback_errors(fallback_outputs: Tuple[Any, ...]) -> Callable:
    """
    A decorator to catch and log exceptions in Dash callbacks.

    If an exception occurs, it logs the error and returns the predefined safe
    fallback outputs.

    Args:
        fallback_outputs (list): A list of safe fallback outputs to return
            in case of an exception.

    Returns:
        Callable: A decorator that catches and logs exceptions in a Dash callback.
    """
    def decorator(callback_func: Callable) -> Callable:
        @wraps(callback_func)
        def wrapper(*args: Any, **kwargs: Any) -> Tuple[Any, ...]:
            try:
                # execute the original callback function
                return callback_func(*args, **kwargs)
            # catch and log exceptions
            except Exception as e:
                callback_name = callback_func.__name__
                logger.error(
                    f"Error in Dash Callback: '{callback_name}'", 
                    exc_info=True, 
                    # include the inputs that triggered the failure
                    extra={'inputs': args} 
                )
                
                # return the predefined safe fallback outputs
                return fallback_outputs
        return wrapper
    return decorator
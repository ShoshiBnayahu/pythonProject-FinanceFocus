import logging
from functools import wraps
"""
This module defines a decorator for logging function execution.
- `logger`: Decorator function for logging function execution.
This decorator wraps around other async functions to log their execution and any errors that occur.
"""
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s \n %(levelname)s :  %(message)s')
def logger(func):
    """
           Decorator function for logging function execution.
           This decorator wraps around other async functions to log their execution and any errors that occur.
           Args:
           - func: The function to be wrapped and logged.
           Returns:
           - wrapper: The wrapped function with logging functionality.
           """
    @wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            result = await func(*args, **kwargs)
            logging.info(f"{func.__name__}() executed successfully\nresult: {result}")
            return result
        except Exception as e:
            logging.error(f"An error occurred during {func.__name__}()\ndetails: {e}")
            raise e
    return wrapper





import logging
from functools import wraps

def logger(func):
    logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s \n %(levelname)s :  %(message)s')
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


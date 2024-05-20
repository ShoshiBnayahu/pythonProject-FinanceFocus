
import logging
from functools import wraps

def logger(func):
    logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    @wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            result = await func(*args, **kwargs)
            logging.info(f"{func.__name__} executed successfully\nresult: {result}")
            return result
        except Exception as e:
            logging.error(f"An error occurred during {func.__name__}: {e}")
            raise e
    return wrapper

# def userExist(func):
#     @wraps(func)
#     async def wrapper(user_id,*args,**kwargs):
#         await user_service.get_user_by_id(user_id)
#         result = await func(user_id,*args, **kwargs)
#         return result
#     return wrapper

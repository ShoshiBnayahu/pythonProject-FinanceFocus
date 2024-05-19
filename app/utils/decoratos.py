from functools import wraps

def logger(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            result = await func(*args, **kwargs)
            print(f"Message: {func.__name__} executed successfully")
            return result
        except Exception as e:
            print(f"An error occurred during {func.__name__}: {e}")
            raise e
    return wrapper

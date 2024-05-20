from functools import wraps
# from app.services import user_service

def logger(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            result = await func(*args, **kwargs)
            print(f"Message: {func.__name__} executed successfully")
            print(result)
            return result
        except Exception as e:
            print(f"An error occurred during {func.__name__}: {e}")
            raise e
    return wrapper

# def userExist(func):
#     @wraps(func)
#     async def wrapper(user_id,*args,**kwargs):
#         await user_service.get_user_by_id(user_id)
#         result = await func(user_id,*args, **kwargs)
#         return result
#     return wrapper
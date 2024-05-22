from pymongo import MongoClient
"""
This script initializes a connection to a MongoDB server and accesses specific collections within a database.

- `client`: Establishes a connection to the MongoDB server running on localhost at port 27017.
- `db`: Accesses the 'Finance_Focus' database.
- `users`: Accesses the 'Users' collection within the 'Finance_Focus' database, which stores user data.
- `users_action`: Accesses the 'UsersAction' collection within the 'Finance_Focus' database, which stores user action data.
"""

client = MongoClient("mongodb://localhost:27017/")
db = client['Finance_Focus']
users = db['Users']
users_action = db['UsersAction']
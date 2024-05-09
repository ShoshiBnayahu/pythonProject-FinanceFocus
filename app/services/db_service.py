from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client['FinanceFocus']
users = db['Users']
users_budget = db['UsersBudget']

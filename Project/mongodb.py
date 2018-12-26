import pymongo
import pandas as pd

class Mongo:
    my_client = pymongo.MongoClient("mongodb://localhost:27017/")
    RazeShop_database = my_client["RazeShop_Database"]
    Users_database = my_client["Users_Database"]

    prod_inf = RazeShop_database["product_information"]
    user_inf = Users_database["user_information"]

    prod_inf_db = pd.DataFrame(list(prod_inf.find({})))







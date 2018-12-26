import pymongo
from Projects import mongodb
import pandas as pd

my_client = pymongo.MongoClient("mongodb://localhost:27017/")
#RazeShop_database = my_client["RazeShop_Database"]
#prod_inf = RazeShop_database["product_information"]


Users_database = my_client["Users_Database"]
user_inf = Users_database["user_information"]

"""list1 = [
         {'_id':1, 'model':'Intel Core I3-6006', 'price':'1500', 'img':'core_i3.png', 'desc':'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Nulla commodi, molestias laborum porro qui, ipsum, fuga nihil voluptas vitae eveniet eos non voluptatibus? Ratione, error. Lorem ipsum dolor sit amet, consectetur adipisicing elit. Maxime voluptate fugiat corporis dolore minima facere magnam impedit nesciunt beatae ut quam, ex, possimus eligendi. Iure.',
         'url':'corei3.html'},
         {'_id':2, 'model':'Acer Aspire ES15', 'price':'1500', 'img':'aspire_es15.png', 'desc':'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Nulla commodi, molestias laborum porro qui, ipsum, fuga nihil voluptas vitae eveniet eos non voluptatibus? Ratione, error. Lorem ipsum dolor sit amet, consectetur adipisicing elit. Maxime voluptate fugiat corporis dolore minima facere magnam impedit nesciunt beatae ut quam, ex, possimus eligendi. Iure.',
         'url':'aspire.html'} ,
         {'_id':3, 'model':'Razer Phone',  'price':'1500', 'img':'razer_phone.png', 'desc':'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Nulla commodi, molestias laborum porro qui, ipsum, fuga nihil voluptas vitae eveniet eos non voluptatibus? Ratione, error. Lorem ipsum dolor sit amet, consectetur adipisicing elit. Maxime voluptate fugiat corporis dolore minima facere magnam impedit nesciunt beatae ut quam, ex, possimus eligendi. Iure.',
         'url':'razer.html'}
]
"""

list1 = [{'username': 'None', 'email': 'None', 'password':'None'}]

user_inf.insert(list1)

# 













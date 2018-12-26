import pandas as pd

class product:
    def __init__(self, model, price, img, desc, url):
        self.model = model
        self.price = price
        self.img = img
        self.desc = desc
        self.url = url

    def prod_inf(self):
        results = pd.DataFrame([self.model, self.price, self.img, self.desc, self.url]).transpose()
        return (results.itertuples())






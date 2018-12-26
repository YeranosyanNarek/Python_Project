from Projects import mongodb as MD

class Register:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def register(self):

        return (MD.Mongo.user_inf.insert({'username': self.username,
                                               'email': self.email,
                                               'password': self.password}))
class Login:

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def email_not(self):
        if len(list(MD.Mongo.user_inf.find({'email': self.email}))) == 0:
            return True

    def email_verif(self):
        if self.email == MD.Mongo.user_inf.find_one({'email': self.email})['email']:
            return True

    def pas_verif(self):
        if self.password == MD.Mongo.user_inf.find_one({'email': self.email})['password']:
            return True

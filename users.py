import json


class User:

    def __init__(self, dct):
        self.email = dct['email']
        self.name = dct['name']
        self.password = dct['password']

    def mult(self, n):
        return [
            User(
                # self.email[:self.email.find('@')] + str(i) + self.email[self.email.find('@'):],
                {'email': str(i) + self.email,
                 "name": self.name + str(i),
                 "password": self.password}
            )
            for i in range(n)
        ]

    def __str__(self):
        return '{' + f'"email":"{self.email}","name":"{self.name}","password":"{self.password}"' + '}'

    def to_dict(self):
        return {'email': self.email, 'name': self.name, 'password': self.password}

    @staticmethod
    def dict_from_json_file(file):
        with open(file) as f:
            temp = json.load(f)
            print(temp)
            return temp

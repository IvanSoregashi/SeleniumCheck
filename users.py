import json


class User:
    def __init__(self, email='email', name='name', password='password'):
        self.email = email
        self.name = name
        self.password = password

    def from_dict(self, dct):
        return self.__init__(self, dct['email'], dct['name'], dct['password'])

    def mult(self, n):
        return [User(str(i) + self.email, self.name + str(i), self.password) for i in range(n)]

    def __str__(self):
        return '{' + f'"email":"{self.email}","name":"{self.name}","password":"{self.password}"' + '}'

    def to_dict(self):
        return {'email': self.email, 'name': self.name, 'password': self.password}

    def from_file(self, file):
        with open(file) as f:
            temp = json.load(f)
            return self.from_dict(self, temp)

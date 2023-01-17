import json
from requests import request
from users import User


class Req:

    def get_user(self, email='email@email.com'):
        url = f"http://users.bugred.ru/tasks/rest/getuser?email={email}"
        return request("POST", url)

    def do_register(self, user=User()):
        url = "http://users.bugred.ru/tasks/rest/doregister"
        payload = json.dumps(user.to_dict())
        headers = {'Content-Type': 'application/json'}
        return request("POST", url, headers=headers, data=payload)

    def create_user(self):
        url = "http://users.bugred.ru/tasks/rest/createuser"
        payload = json.dumps({'email': '', 'name': '', 'companies': [], 'tasks': []})
        headers = {'Content-Type': 'application/json'}
        response = request("POST", url, headers=headers, data=payload)
        return response.text

    def create_company(self):
        url = "http://users.bugred.ru/tasks/rest/createcompany"
        payload = {'company_name': '', 'company_type': '',
                   'company_users': '["@mail.ru", "@mail.ru"]', 'email_owner': '@mail.ru'}
        files = []
        headers = {}
        response = request("POST", url, headers=headers, data=payload, files=files)
        return response.text

    def create_user_with_tasks(self):
        url = "http://users.bugred.ru/tasks/rest/createuserwithtasks"
        payload = json.dumps({
            "email": "@mail.ru",
            "name": "",
            "tasks": [
                {
                    "title": "first",
                    "description": ""
                },
                {
                    "title": "second",
                    "description": ""
                }
            ]
        })
        headers = {'Content-Type': 'application/json'}
        response = request("POST", url, headers=headers, data=payload)
        return response.text


r = Req()
usr = User()
usr.from_file('user.json')
resp = r.do_register(usr)
print(resp.text)
print(resp.content)
print(resp.content.decode('unicode-escape'))

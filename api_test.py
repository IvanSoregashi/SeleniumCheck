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
        payload = json.dumps({"email": "dododo@mail.ru", "name": "Stefan", "companies": [10], "tasks": [12]})
        headers = {'Content-Type': 'application/json'}
        response = request("POST", url, headers=headers, data=payload)
        return response.text

    def create_company(self):
        url = "http://users.bugred.ru/tasks/rest/createcompany"
        payload = {'company_name': 'zaraaa', 'company_type': 'ООО',
                   'company_users': '["elena345@mail.ru", "day234@mail.ru"]', 'email_owner': 'alyona111@mail.ru'}
        files = []
        headers = {}
        response = request("POST", url, headers=headers, data=payload, files=files)
        return response.text

    def create_user_with_tasks(self):
        url = "http://users.bugred.ru/tasks/rest/createuserwithtasks"
        payload = json.dumps({
            "email": "ghilbertt@mail.ru",
            "name": "Elina",
            "tasks": [
                {
                    "title": "Первая задача",
                    "description": "Первая задача 11"
                },
                {
                    "title": "Вторая задача",
                    "description": "Вторая задача 11"
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

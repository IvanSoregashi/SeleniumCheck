from requests import request

email = 'email@email.com'
url = f"http://users.bugred.ru/tasks/rest/getuser?email={email}"

payload = ""
headers = {}

response = request("POST", url)

print(response.text)

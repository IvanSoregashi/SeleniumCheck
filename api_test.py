from requests import request

url = f"http://users.bugred.ru/tasks/rest/getuser?email={email}"

payload = ""
headers = {}

response = request("POST", url)

print(response.text)

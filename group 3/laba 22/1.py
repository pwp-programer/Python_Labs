import requests, json

response = requests.get("https://www.google.com/")
print(response)
print(requests.get("https://github.com/pwp-programers/"))
print(requests.get("https://api.github.com/user"))


a = response.status_code
b = response.headers['date']
c = response.headers['content-type']
print(a, b, c)



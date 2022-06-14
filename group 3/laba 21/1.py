import requests

r = requests.post('https://httpbin.org/post', data = {'key':'value'})  
print(r)
r = requests.put('https://httpbin.org/put', data = {'key':'value'})  
print(r)
r = requests.delete('https://httpbin.org/delete')  
print(r)
r = requests.head('https://httpbin.org/get')  
print(r)
r = requests.options('https://httpbin.org/get')  
print(r)

from urllib.parse import urlparse

url = urlparse("www.google.com")
create = url[0] + url[1] + url[2]
print(create)
